# KdpWriteMachineSpecificRegister

- RVA: `0x00B88A90`–`0x00B88AF8` (길이 `104` bytes)
- VA: `0x0000000140B88A90`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BDB64`
- 디코드: `27`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B88ACA` → [KdpSysWriteMsr](../../text/5B/KdpSysWriteMsr_function_005B13A4.md) (function, `0x005B13A4`)
- `0x00B88AE5` → `kdcom.dll!KdSendPacket` (import, 간접 대상; import `kdcom.dll!KdSendPacket`)

### Direct callers
- [KdpSendWaitContinue](KdpSendWaitContinue_function_00B8A32C.md) at `0x00B8A595`

### Static image references
- `0x00B88AD5` → RVA `0x00F475E0` (`.data`; read)
- `0x00B88AE5` → RVA `0x001516C0` (`kdcom.dll!KdSendPacket (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B88ACA` → [KdpSysWriteMsr](../../text/5B/KdpSysWriteMsr_function_005B13A4.md) (`PAGEKD` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B88A90  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00B88A95  53                              push rbx
00B88A96  48 83 EC 30                     sub rsp, 0x30
00B88A9A  B8 38 00 00 00                  mov eax, 0x38
00B88A9F  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00B88AA4  0F 57 C0                        xorps xmm0, xmm0
00B88AA7  48 8B D9                        mov rbx, rcx
00B88AAA  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00B88AAF  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00B88AB4  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00B88AB7  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00B88ABB  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00B88ABE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B88AC3  8B 49 10                        mov ecx, dword ptr [rcx + 0x10]
00B88AC6  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B88ACA  E8 D5 88 A2 FF                  call 0x1405b13a4
00B88ACF  45 33 C0                        xor r8d, r8d
00B88AD2  89 43 08                        mov dword ptr [rbx + 8], eax
00B88AD5  4C 8D 0D 04 EB 3B 00            lea r9, [rip + 0x3beb04]
00B88ADC  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00B88AE1  41 8D 48 02                     lea ecx, [r8 + 2]
00B88AE5  48 FF 15 D4 8B 5C FF            call qword ptr [rip - 0xa3742c]
00B88AEC  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B88AF1  48 83 C4 30                     add rsp, 0x30
00B88AF5  5B                              pop rbx
00B88AF6  C3                              ret
00B88AF7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpWriteMachineSpecificRegister(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p1C;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 56;
    v_stack_p1C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    v_stack_m10 = a1;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
    result = KdpSysWriteMsr((unsigned int)(*(unsigned int *)(a1 + 16)), v_stack_p18, a3, a4);
    a3 = 0;
    *(unsigned int *)(a1 + 8) = (unsigned int)(result);
    result = kdcom_dll_KdSendPacket(a3 + 2, v_stack_m18, a3, v_rip + 3926788);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdpWriteMachineSpecificRegister(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p18;
    uint32_t v_stack_p1C;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 56;
    v_stack_p1C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    v_stack_m10 = Arg1;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)));
    result = KdpSysWriteMsr((uint32_t)(*(uint32_t *)(arg1 + 0x10)), v_stack_p18, Arg3, a4);
    Arg3 = 0;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
    result = kernel_indirect_call(Arg3 + 2, v_stack_m18, Arg3, v_rip + 3926788);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B88A90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B88A90[BB_00B88A90]
  bb_00B88AF7[BB_00B88AF7]
```
