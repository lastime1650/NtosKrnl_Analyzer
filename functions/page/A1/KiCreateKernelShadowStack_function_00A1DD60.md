# KiCreateKernelShadowStack

- RVA: `0x00A1DD60`–`0x00A1DDBA` (길이 `90` bytes)
- VA: `0x0000000140A1DD60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `23`개 명령, `90/90` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A1DD8B` → [MmCreateKernelStack](../../text/33/MmCreateKernelStack_function_00337D20.md) (function, `0x00337D20`)

### Direct callers
- [KiAllocateProcessorStacks](../../text/5B/KiAllocateProcessorStacks_function_005B6D74.md) at `0x005B6E4C`
- [KiAllocateProcessorStacks](../../text/5B/KiAllocateProcessorStacks_function_005B6D74.md) at `0x005B6EC8`
- [KiAllocateProcessorHiberSwapShadowStacks](../../text/5B/KiAllocateProcessorHiberSwapShadowStacks_function_005BD754.md) at `0x005BD7B4`
- [KeInitThread](../../pagelk/B7/KeInitThread_function_00B78450.md) at `0x00B7883C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A1DD8B` → [MmCreateKernelStack](../../text/33/MmCreateKernelStack_function_00337D20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1DD60  48 8B C4                        mov rax, rsp
00A1DD63  48 83 EC 58                     sub rsp, 0x58
00A1DD67  83 60 D4 00                     and dword ptr [rax - 0x2c], 0
00A1DD6B  0F 57 C0                        xorps xmm0, xmm0
00A1DD6E  48 83 60 F0 00                  and qword ptr [rax - 0x10], 0
00A1DD73  48 89 48 D8                     mov qword ptr [rax - 0x28], rcx
00A1DD77  48 8D 48 C8                     lea rcx, [rax - 0x38]
00A1DD7B  F3 0F 7F 40 E0                  movdqu xmmword ptr [rax - 0x20], xmm0
00A1DD80  44 89 40 C8                     mov dword ptr [rax - 0x38], r8d
00A1DD84  89 50 CC                        mov dword ptr [rax - 0x34], edx
00A1DD87  44 89 48 D0                     mov dword ptr [rax - 0x30], r9d
00A1DD8B  E8 90 9F 91 FF                  call 0x140337d20
00A1DD90  85 C0                           test eax, eax
00A1DD92  78 20                           js 0x140a1ddb4
00A1DD94  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00A1DD9C  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00A1DDA1  48 89 0A                        mov qword ptr [rdx], rcx
00A1DDA4  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00A1DDAC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00A1DDB1  48 89 0A                        mov qword ptr [rdx], rcx
00A1DDB4  48 83 C4 58                     add rsp, 0x58
00A1DDB8  C3                              ret
00A1DDB9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCreateKernelShadowStack(__int64 a1, int a2, int a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;

    v_rsp = (v_rsp) - (88);
    *(unsigned __int64 *)(v_rsp - 40) = a1;
    *(unsigned __int64 *)(v_rsp - 32) = v_xmm0;
    *(unsigned int *)(v_rsp - 56) = a3;
    *(unsigned int *)(v_rsp - 52) = a2;
    *(unsigned int *)(v_rsp - 48) = a4;
    result = MmCreateKernelStack(v_rsp - 56, a2, a3, a4);
    if (!(sign_flag)) {
        a2 = a5;
        a1 = v_stack_m20;
        *(unsigned __int64 *)(a2) = a1;
        a2 = a6;
        a1 = v_stack_m18;
        *(unsigned __int64 *)(a2) = a1;
    }
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiCreateKernelShadowStack(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;

    local_rsp = (local_rsp) - (88);
    *(uint64_t *)(local_rsp - 0x28) = Arg1;
    *(uint64_t *)(local_rsp - 0x20) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x38) = Arg3;
    *(uint32_t *)(local_rsp - 0x34) = Arg2;
    *(uint32_t *)(local_rsp - 0x30) = Arg4;
    result = MmCreateKernelStack(local_rsp - 56, Arg2, Arg3, Arg4);
    if (!(sign_flag)) {
        Arg2 = Arg5;
        Arg1 = v_stack_m20;
        *(uint64_t *)(Arg2) = Arg1;
        Arg2 = Arg6;
        Arg1 = v_stack_m18;
        *(uint64_t *)(Arg2) = Arg1;
    }
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1DD60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A1DD60[BB_00A1DD60]
  bb_00A1DD94[BB_00A1DD94]
  bb_00A1DDB4[BB_00A1DDB4]
  bb_00A1DDB9[BB_00A1DDB9]
  bb_00A1DD60 -->|branch| bb_00A1DDB4
  bb_00A1DD60 -->|fallthrough| bb_00A1DD94
  bb_00A1DD94 -->|flow| bb_00A1DDB4
```
