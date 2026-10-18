# CmFcpManagerDrainUsageNotifications

- RVA: `0x00A451BC`–`0x00A45258` (길이 `156` bytes)
- VA: `0x0000000140A451BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF2C0`
- 디코드: `45`개 명령, `156/156` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A451EB` → [RtlUpdateSwapReference](RtlUpdateSwapReference_function_00A45260.md) (function, `0x00A45260`)
- `0x00A45204` → [RtlpFcBufferManagerReferenceBuffers](../../text/4A/RtlpFcBufferManagerReferenceBuffers_function_004A73B8.md) (function, `0x004A73B8`)
- `0x00A4522B` → [RtlpFcDrainDelayedUsageReportBuffer](RtlpFcDrainDelayedUsageReportBuffer_function_00A452D0.md) (function, `0x00A452D0`)
- `0x00A45236` → [RtlpFcBufferManagerDereferenceBuffers](../../text/37/RtlpFcBufferManagerDereferenceBuffers_function_00378D84.md) (function, `0x00378D84`)
- `0x00A45251` → [CmFcpManagerArmFeatureUsageRetryTimer](../../text/66/CmFcpManagerArmFeatureUsageRetryTimer_function_0066B2DC.md) (function, `0x0066B2DC`)

### Direct callers
- [CmFcManagerDrainAllFeatureUsageNotifications](../7F/CmFcManagerDrainAllFeatureUsageNotifications_function_007F439C.md) at `0x007F43FF`
- [CmFcManagerDrainAllFeatureUsageNotifications](../7F/CmFcManagerDrainAllFeatureUsageNotifications_function_007F439C.md) at `0x007F440D`
- [CmFcpManagerRetryUsageNotificationsWorker](../7F/CmFcpManagerRetryUsageNotificationsWorker_function_007F56D0.md) at `0x007F573E`
- [CmFcpManagerRetryUsageNotificationsWorker](../7F/CmFcpManagerRetryUsageNotificationsWorker_function_007F56D0.md) at `0x007F5748`
- [CmFcpManagerSoftwareHiveReady](../7F/CmFcpManagerSoftwareHiveReady_function_007F5790.md) at `0x007F580C`
- [CmFcpManagerSoftwareHiveReady](../7F/CmFcpManagerSoftwareHiveReady_function_007F5790.md) at `0x007F5816`
- [CmFcpManagerDrainUsageNotificationsWorker](CmFcpManagerDrainUsageNotificationsWorker_function_00A45110.md) at `0x00A45177`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A45204` → [RtlpFcBufferManagerReferenceBuffers](../../text/4A/RtlpFcBufferManagerReferenceBuffers_function_004A73B8.md) (`PAGE` → `.text`)
  - `0x00A45236` → [RtlpFcBufferManagerDereferenceBuffers](../../text/37/RtlpFcBufferManagerDereferenceBuffers_function_00378D84.md) (`PAGE` → `.text`)
  - `0x00A45251` → [CmFcpManagerArmFeatureUsageRetryTimer](../../text/66/CmFcpManagerArmFeatureUsageRetryTimer_function_0066B2DC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A451BC  40 53                           push rbx
00A451BE  55                              push rbp
00A451BF  56                              push rsi
00A451C0  57                              push rdi
00A451C1  41 56                           push r14
00A451C3  48 83 EC 30                     sub rsp, 0x30
00A451C7  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
00A451CD  40 8A EA                        mov bpl, dl
00A451D0  83 64 24 60 00                  and dword ptr [rsp + 0x60], 0
00A451D5  4C 8B F1                        mov r14, rcx
00A451D8  48 81 C1 78 01 00 00            add rcx, 0x178
00A451DF  48 8B 19                        mov rbx, qword ptr [rcx]
00A451E2  83 E3 01                        and ebx, 1
00A451E5  8D 53 FF                        lea edx, [rbx - 1]
00A451E8  83 E2 01                        and edx, 1
00A451EB  E8 70 00 00 00                  call 0x140a45260
00A451F0  49 8D B6 88 00 00 00            lea rsi, [r14 + 0x88]
00A451F7  48 8B CE                        mov rcx, rsi
00A451FA  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00A451FF  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00A45204  E8 AF 21 A6 FF                  call 0x1404a73b8
00A45209  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00A4520E  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A45213  49 8B 8C DE A0 01 00 00         mov rcx, qword ptr [r14 + rbx*8 + 0x1a0]
00A4521B  40 8A D5                        mov dl, bpl
00A4521E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A45223  4C 8B 4F 40                     mov r9, qword ptr [rdi + 0x40]
00A45227  4C 8B 47 38                     mov r8, qword ptr [rdi + 0x38]
00A4522B  E8 A0 00 00 00                  call 0x140a452d0
00A45230  48 8B D7                        mov rdx, rdi
00A45233  48 8B CE                        mov rcx, rsi
00A45236  E8 49 3B 93 FF                  call 0x140378d84
00A4523B  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
00A45240  77 0C                           ja 0x140a4524e
00A45242  48 83 C4 30                     add rsp, 0x30
00A45246  41 5E                           pop r14
00A45248  5F                              pop rdi
00A45249  5E                              pop rsi
00A4524A  5D                              pop rbp
00A4524B  5B                              pop rbx
00A4524C  C3                              ret
00A4524D  CC                              int3
00A4524E  49 8B CE                        mov rcx, r14
00A45251  E8 86 60 C2 FF                  call 0x14066b2dc
00A45256  EB EA                           jmp 0x140a45242
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpManagerDrainUsageNotifications(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (48);
    a1 = (a1) + (376);
    v_rbx = (unsigned int)((*(unsigned __int64 *)(a1)) & (1));
    a2 = (unsigned int)((v_rbx - 1) & (1));
    result = RtlUpdateSwapReference(a1, a2, a3, a4);
    result = RtlpFcBufferManagerReferenceBuffers(a1 + 136, v_stack_p20, v_stack_p18, a4);
    v_stack_m38 = v_stack_p8;
    result = RtlpFcDrainDelayedUsageReportBuffer(*(unsigned __int64 *)(a1 + v_rbx * 8 + 416), a2, *(unsigned __int64 *)(v_stack_p18 + 56), *(unsigned __int64 *)(v_stack_p18 + 64));
    result = RtlpFcBufferManagerDereferenceBuffers(a1 + 136, v_stack_p18, *(unsigned __int64 *)(v_stack_p18 + 56), *(unsigned __int64 *)(v_stack_p18 + 64));
    if (v_stack_p8 > 0) goto loc_00A4524E;
loc_00A45242:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00A4524E:
    result = CmFcpManagerArmFeatureUsageRetryTimer(a1, v_stack_p18, *(unsigned __int64 *)(v_stack_p18 + 56), *(unsigned __int64 *)(v_stack_p18 + 64));
    goto loc_00A45242;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpManagerDrainUsageNotifications(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (48);
    Arg1 = (Arg1) + (376);
    local_rbx = (uint32_t)((*(uint64_t *)(arg1)) & (1));
    Arg2 = (uint32_t)((local_rbx - 1) & (1));
    result = RtlUpdateSwapReference(Arg1, Arg2, a3, a4);
    result = RtlpFcBufferManagerReferenceBuffers(Arg1 + 136, v_stack_p20, v_stack_p18, a4);
    v_stack_m38 = v_stack_p8;
    result = RtlpFcDrainDelayedUsageReportBuffer(*(uint64_t *)(arg1 + local_rbx * 8 + 0x1A0), Arg2, *(uint64_t *)(v_stack_p18 + 0x38), *(uint64_t *)(v_stack_p18 + 0x40));
    result = RtlpFcBufferManagerDereferenceBuffers(Arg1 + 136, v_stack_p18, *(uint64_t *)(v_stack_p18 + 0x38), *(uint64_t *)(v_stack_p18 + 0x40));
    if (v_stack_p8 > 0) goto loc_00A4524E;
loc_00A45242:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00A4524E:
    result = CmFcpManagerArmFeatureUsageRetryTimer(Arg1, v_stack_p18, *(uint64_t *)(v_stack_p18 + 0x38), *(uint64_t *)(v_stack_p18 + 0x40));
    goto loc_00A45242;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |
| `Arg1` | `+ 0x1A0 + rbx*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A451BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A451BC[BB_00A451BC]
  bb_00A45242[BB_00A45242]
  bb_00A4524D[BB_00A4524D]
  bb_00A4524E[BB_00A4524E]
  bb_00A451BC -->|branch| bb_00A4524E
  bb_00A451BC -->|fallthrough| bb_00A45242
  bb_00A4524D -->|flow| bb_00A4524E
  bb_00A4524E -->|branch| bb_00A45242
```
