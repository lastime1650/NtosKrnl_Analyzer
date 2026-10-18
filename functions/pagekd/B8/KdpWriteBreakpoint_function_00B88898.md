# KdpWriteBreakpoint

- RVA: `0x00B88898`–`0x00B88904` (길이 `108` bytes)
- VA: `0x0000000140B88898`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `29`개 명령, `108/108` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B888C7` → [KdpAddBreakpoint](KdpAddBreakpoint_function_00B897E8.md) (function, `0x00B897E8`)
- `0x00B888F1` → `kdcom.dll!KdSendPacket` (import, 간접 대상; import `kdcom.dll!KdSendPacket`)

### Direct callers
- [KdpSendWaitContinue](KdpSendWaitContinue_function_00B8A32C.md) at `0x00B8A501`

### Static image references
- `0x00B888CF` → RVA `0x00F475E0` (`.data`; read)
- `0x00B888F1` → RVA `0x001516C0` (`kdcom.dll!KdSendPacket (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B88898  40 53                           push rbx
00B8889A  48 83 EC 30                     sub rsp, 0x30
00B8889E  0F 57 C0                        xorps xmm0, xmm0
00B888A1  48 8B D9                        mov rbx, rcx
00B888A4  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00B888A9  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B888AE  B8 38 00 00 00                  mov eax, 0x38
00B888B3  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B888B7  45 33 C9                        xor r9d, r9d
00B888BA  41 B0 01                        mov r8b, 1
00B888BD  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00B888C2  BA CC 00 00 00                  mov edx, 0xcc
00B888C7  E8 1C 0F 00 00                  call 0x140b897e8
00B888CC  89 43 18                        mov dword ptr [rbx + 0x18], eax
00B888CF  4C 8D 0D 0A ED 3B 00            lea r9, [rip + 0x3bed0a]
00B888D6  F7 D8                           neg eax
00B888D8  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00B888DD  1B C9                           sbb ecx, ecx
00B888DF  45 33 C0                        xor r8d, r8d
00B888E2  F7 D1                           not ecx
00B888E4  81 E1 01 00 00 C0               and ecx, 0xc0000001
00B888EA  89 4B 08                        mov dword ptr [rbx + 8], ecx
00B888ED  41 8D 48 02                     lea ecx, [r8 + 2]
00B888F1  48 FF 15 C8 8D 5C FF            call qword ptr [rip - 0xa37238]
00B888F8  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B888FD  48 83 C4 30                     add rsp, 0x30
00B88901  5B                              pop rbx
00B88902  C3                              ret
00B88903  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpWriteBreakpoint(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_stack_m18 = v_xmm0;
    v_stack_m10 = a1;
    a4 = 0;
    v_stack_m18 = 56;
    result = KdpAddBreakpoint(*(unsigned __int64 *)(a1 + 16), 204, 1, a4);
    *(unsigned int *)(a1 + 24) = (unsigned int)(result);
    result = (unsigned int)(-(result));
    a3 = 0;
    a1 = (unsigned int)(~(*(unsigned __int64 *)(a1 + 16)));
    a1 = (unsigned int)((a1) & (0xC0000001ULL));
    *(unsigned int *)(a1 + 8) = (unsigned int)(a1);
    result = kdcom_dll_KdSendPacket(a3 + 2, v_stack_m18, a3, v_rip + 3927306);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdpWriteBreakpoint(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    v_stack_m18 = v_xmm0;
    v_stack_m10 = Arg1;
    Arg4 = 0;
    v_stack_m18 = 56;
    result = KdpAddBreakpoint(*(uint64_t *)(arg1 + 0x10), 204, 1, Arg4);
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)(result);
    result = (uint32_t)(-(result));
    Arg3 = 0;
    Arg1 = (uint32_t)(~(*(uint64_t *)(arg1 + 0x10)));
    Arg1 = (uint32_t)((Arg1) & (0xC0000001ULL));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(Arg1);
    result = kernel_indirect_call(Arg3 + 2, v_stack_m18, Arg3, v_rip + 3927306);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B88898&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B88898[BB_00B88898]
  bb_00B88903[BB_00B88903]
```
