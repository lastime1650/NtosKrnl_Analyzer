# EtwpSendSessionNotification

- RVA: `0x009BFE28`–`0x009BFEE9` (길이 `193` bytes)
- VA: `0x00000001409BFE28`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F4FC`
- 디코드: `44`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009BFE68` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009BFEB6` → [EtwpNotifyGuid](../8C/EtwpNotifyGuid_function_008C8110.md) (function, `0x008C8110`)
- `0x009BFEC6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpStopLoggerInstance](EtwpStopLoggerInstance_function_009BEB94.md) at `0x009BEF45`
- [EtwpRealtimeFlushSavedBuffers](EtwpRealtimeFlushSavedBuffers_function_009BF1B0.md) at `0x009BF30F`
- [EtwpFlushBuffer](EtwpFlushBuffer_function_009BF570.md) at `0x009BF6AA`
- [EtwpFlushBuffer](EtwpFlushBuffer_function_009BF570.md) at `0x009BF6EA`
- [EtwpCreateLogFile](../9C/EtwpCreateLogFile_function_009C035C.md) at `0x009C07D8`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9AD43`
- [sub_00B2EA5E](../B2/Unknown_function_00B2EA5E.md) at `0x00B2EAF9`

### Static image references
- `0x009BFE37` → RVA `0x00E0A740` (`.data`; read)
- `0x009BFE6D` → RVA `0x00013DA8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009BFE68` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009BFEC6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009BFE28  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009BFE2D  55                              push rbp
009BFE2E  56                              push rsi
009BFE2F  57                              push rdi
009BFE30  48 81 EC 90 00 00 00            sub rsp, 0x90
009BFE37  48 8B 05 02 A9 44 00            mov rax, qword ptr [rip + 0x44a902]
009BFE3E  48 33 C4                        xor rax, rsp
009BFE41  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009BFE49  0F B7 19                        movzx ebx, word ptr [rcx]
009BFE4C  41 8B E8                        mov ebp, r8d
009BFE4F  8B F2                           mov esi, edx
009BFE51  48 8B F9                        mov rdi, rcx
009BFE54  66 85 DB                        test bx, bx
009BFE57  0F 84 82 00 00 00               je 0x1409bfedf
009BFE5D  33 D2                           xor edx, edx
009BFE5F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
009BFE64  44 8D 42 60                     lea r8d, [rdx + 0x60]
009BFE68  E8 D3 6D D0 FF                  call 0x1406c6c40
009BFE6D  0F 10 05 34 3F 65 FF            movups xmm0, xmmword ptr [rip - 0x9ac0cc]
009BFE74  48 8B 8F 50 05 00 00            mov rcx, qword ptr [rdi + 0x550]
009BFE7B  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
009BFE80  0F B7 C3                        movzx eax, bx
009BFE83  45 33 C0                        xor r8d, r8d
009BFE86  F3 0F 7F 44 24 48               movdqu xmmword ptr [rsp + 0x48], xmm0
009BFE8C  C7 44 24 24 60 00 00 00         mov dword ptr [rsp + 0x24], 0x60
009BFE94  0F 10 87 14 01 00 00            movups xmm0, xmmword ptr [rdi + 0x114]
009BFE9B  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
009BFEA3  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009BFEA8  F3 0F 7F 44 24 58               movdqu xmmword ptr [rsp + 0x58], xmm0
009BFEAE  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
009BFEB2  89 6C 24 6C                     mov dword ptr [rsp + 0x6c], ebp
009BFEB6  E8 55 82 F0 FF                  call 0x1408c8110
009BFEBB  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009BFEC3  48 33 CC                        xor rcx, rsp
009BFEC6  E8 75 C7 CE FF                  call 0x1406ac640
009BFECB  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
009BFED3  48 81 C4 90 00 00 00            add rsp, 0x90
009BFEDA  5F                              pop rdi
009BFEDB  5E                              pop rsi
009BFEDC  5D                              pop rbp
009BFEDD  C3                              ret
009BFEDE  CC                              int3
009BFEDF  BB FF FF 00 00                  mov ebx, 0xffff
009BFEE4  E9 74 FF FF FF                  jmp 0x1409bfe5d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpSendSessionNotification(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m84;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 4499714)) ^ (v_rsp);
    v_stack_m28 = result;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_009BFEDF;
loc_009BFE5D:
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 96, a4);
    a3 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m84 = 96;
    v_stack_m88 = 7;
    v_stack_m38 = (unsigned __int16)(*(unsigned __int16 *)(a1));
    v_stack_m50 = v_xmm0;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m3C = (unsigned int)((unsigned int)(a3));
    result = EtwpNotifyGuid(*(unsigned __int64 *)(a1 + 1360), v_stack_m88, a3, a4);
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m88, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
loc_009BFEDF:
    goto loc_009BFE5D;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpSendSessionNotification(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint32_t v_stack_m84;
    uint64_t v_stack_m88;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x44A902)) ^ (local_rsp);
    v_stack_m28 = result;
    if ((uint16_t)(*(uint16_t *)(arg1)) == 0) goto loc_009BFEDF;
loc_009BFE5D:
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 96, a4);
    Arg3 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m84 = 96;
    v_stack_m88 = 7;
    v_stack_m38 = (uint16_t)(*(uint16_t *)(arg1));
    v_stack_m50 = v_xmm0;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m3C = (uint32_t)((uint32_t)(Arg3));
    result = EtwpNotifyGuid(*(uint64_t *)(arg1 + 0x550), v_stack_m88, Arg3, a4);
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m88, Arg3, a4);
    local_rsp = (local_rsp) + (144);
    return result;
loc_009BFEDF:
    goto loc_009BFE5D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x114` | `128` | `R` |
| `Arg1` | `+ 0x550` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BFE28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009BFE28[BB_009BFE28]
  bb_009BFE5D[BB_009BFE5D]
  bb_009BFEDE[BB_009BFEDE]
  bb_009BFEDF[BB_009BFEDF]
  bb_009BFE28 -->|branch| bb_009BFEDF
  bb_009BFE28 -->|fallthrough| bb_009BFE5D
  bb_009BFEDE -->|flow| bb_009BFEDF
  bb_009BFEDF -->|branch| bb_009BFE5D
```
