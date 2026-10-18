# PopUmpoSendLegacyEvent

- RVA: `0x00AA48E8`–`0x00AA4947` (길이 `95` bytes)
- VA: `0x0000000140AA48E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB554`
- 디코드: `27`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AA4902` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AA492E` → [PopUmpoSendPowerMessage](../../text/23/PopUmpoSendPowerMessage_function_00230730.md) (function, `0x00230730`)
- `0x00AA4940` → [PfIoPowerEventNotify](../75/PfIoPowerEventNotify_function_00750784.md) (function, `0x00750784`)

### Direct callers
- [PopDirectedDripsSendSuspendResumeNotification](../75/PopDirectedDripsSendSuspendResumeNotification_function_00757CCC.md) at `0x00757D4A`
- [PopDirectedDripsSendSuspendResumeNotification](../75/PopDirectedDripsSendSuspendResumeNotification_function_00757CCC.md) at `0x00757D6D`
- [PopSendSuspendResumeServiceNotification](../75/PopSendSuspendResumeServiceNotification_function_0075ED9C.md) at `0x0075EE38`
- [PopSendSuspendResumeServiceNotification](../75/PopSendSuspendResumeServiceNotification_function_0075ED9C.md) at `0x0075EE48`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x0095711E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AA4902` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AA492E` → [PopUmpoSendPowerMessage](../../text/23/PopUmpoSendPowerMessage_function_00230730.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA48E8  40 53                           push rbx
00AA48EA  48 83 EC 70                     sub rsp, 0x70
00AA48EE  33 C0                           xor eax, eax
00AA48F0  48 8B D9                        mov rbx, rcx
00AA48F3  33 D2                           xor edx, edx
00AA48F5  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00AA48F9  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00AA48FE  44 8D 40 44                     lea r8d, [rax + 0x44]
00AA4902  E8 39 23 C2 FF                  call 0x1406c6c40
00AA4907  80 7B 0C 00                     cmp byte ptr [rbx + 0xc], 0
00AA490B  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AA490E  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
00AA4916  F3 0F 7F 44 24 28               movdqu xmmword ptr [rsp + 0x28], xmm0
00AA491C  75 1C                           jne 0x140aa493a
00AA491E  44 8A 43 0D                     mov r8b, byte ptr [rbx + 0xd]
00AA4922  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00AA4927  45 33 C9                        xor r9d, r9d
00AA492A  41 8D 51 48                     lea edx, [r9 + 0x48]
00AA492E  E8 FD BD 78 FF                  call 0x140230730
00AA4933  48 83 C4 70                     add rsp, 0x70
00AA4937  5B                              pop rbx
00AA4938  C3                              ret
00AA4939  CC                              int3
00AA493A  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00AA493D  45 33 C0                        xor r8d, r8d
00AA4940  E8 3F BE CA FF                  call 0x140750784
00AA4945  EB D7                           jmp 0x140aa491e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopUmpoSendLegacyEvent(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (112);
    result = 0;
    a2 = 0;
    v_stack_m54 = 0;
    result = memset(v_stack_m58, a2, result + 68, a4);
    v_stack_m58 = 7;
    v_stack_m50 = v_xmm0;
    if ((*(unsigned __int8 *)(a1 + 12)) != 0) goto loc_00AA493A;
loc_00AA491E:
    a4 = 0;
    result = PopUmpoSendPowerMessage(v_stack_m58, a4 + 72, *(unsigned __int8 *)(a1 + 13), a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_00AA493A:
    a3 = 0;
    result = PfIoPowerEventNotify((unsigned int)(*(unsigned int *)(a1 + 4)), a4 + 72, a3, a4);
    goto loc_00AA491E;
}
```

## 5. (Beta) C Style

```c
int64_t PopUmpoSendLegacyEvent(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (112);
    result = 0;
    Arg2 = 0;
    v_stack_m54 = 0;
    result = memset(v_stack_m58, Arg2, result + 68, Arg4);
    v_stack_m58 = 7;
    v_stack_m50 = v_xmm0;
    if ((*(uint8_t *)(arg1 + 0xC)) != 0) goto loc_00AA493A;
loc_00AA491E:
    Arg4 = 0;
    result = PopUmpoSendPowerMessage(v_stack_m58, Arg4 + 72, *(uint8_t *)(arg1 + 0xD), Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_00AA493A:
    Arg3 = 0;
    result = PfIoPowerEventNotify((uint32_t)(*(uint32_t *)(arg1 + 0x4)), Arg4 + 72, Arg3, Arg4);
    goto loc_00AA491E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA48E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA48E8[BB_00AA48E8]
  bb_00AA491E[BB_00AA491E]
  bb_00AA4939[BB_00AA4939]
  bb_00AA493A[BB_00AA493A]
  bb_00AA48E8 -->|branch| bb_00AA493A
  bb_00AA48E8 -->|fallthrough| bb_00AA491E
  bb_00AA4939 -->|flow| bb_00AA493A
  bb_00AA493A -->|branch| bb_00AA491E
```
