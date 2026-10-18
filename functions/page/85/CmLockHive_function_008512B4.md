# CmLockHive

- RVA: `0x008512B4`–`0x00851300` (길이 `76` bytes)
- VA: `0x00000001408512B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008512CD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008512E6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CmpWaitForLateUnloadWorker](../../text/45/CmpWaitForLateUnloadWorker_function_004573F8.md) at `0x0045740A`
- [CmpWaitForLateUnloadWorker](../../text/45/CmpWaitForLateUnloadWorker_function_004573F8.md) at `0x0045747E`
- [CmpDoQueueLateUnloadWorker](../84/CmpDoQueueLateUnloadWorker_function_0084FB18.md) at `0x0084FB21`
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00850792`
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x008510D5`
- [CmpCloseKeyObject](../86/CmpCloseKeyObject_function_00863AD0.md) at `0x00863C30`
- [sub_0086560A](../86/Unknown_function_0086560A.md) at `0x00865811`
- [sub_008C7238](../8C/Unknown_function_008C7238.md) at `0x008C7288`
- [CmpFlushNotify](../9B/CmpFlushNotify_function_009B36A8.md) at `0x009B36DF`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCBFE`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCC0B`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCC22`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCC2F`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCC51`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008512CD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008512E6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008512B4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008512B9  57                              push rdi
008512BA  48 83 EC 20                     sub rsp, 0x20
008512BE  48 8D B9 90 06 00 00            lea rdi, [rcx + 0x690]
008512C5  45 33 C0                        xor r8d, r8d
008512C8  48 8B CF                        mov rcx, rdi
008512CB  33 D2                           xor edx, edx
008512CD  E8 5E EF 9B FF                  call 0x140210230
008512D2  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008512D8  48 8B D8                        mov rbx, rax
008512DB  73 0E                           jae 0x1408512eb
008512DD  4C 8B C7                        mov r8, rdi
008512E0  48 8B D0                        mov rdx, rax
008512E3  48 8B CF                        mov rcx, rdi
008512E6  E8 A5 E9 9B FF                  call 0x14020fc90
008512EB  48 85 DB                        test rbx, rbx
008512EE  74 04                           je 0x1408512f4
008512F0  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
008512F4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008512F9  48 83 C4 20                     add rsp, 0x20
008512FD  5F                              pop rdi
008512FE  C3                              ret
008512FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmLockHive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1680, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 1680;
        a2 = result;
        a1 = a1 + 1680;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmLockHive(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1680, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 1680;
        Arg2 = result;
        Arg1 = Arg1 + 1680;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x690` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008512B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008512B4[BB_008512B4]
  bb_008512DD[BB_008512DD]
  bb_008512EB[BB_008512EB]
  bb_008512F0[BB_008512F0]
  bb_008512F4[BB_008512F4]
  bb_008512FF[BB_008512FF]
  bb_008512B4 -->|branch| bb_008512EB
  bb_008512B4 -->|fallthrough| bb_008512DD
  bb_008512DD -->|flow| bb_008512EB
  bb_008512EB -->|branch| bb_008512F4
  bb_008512EB -->|fallthrough| bb_008512F0
  bb_008512F0 -->|flow| bb_008512F4
```
