# CmUnlockHive

- RVA: `0x00851D6C`–`0x00851D9F` (길이 `51` bytes)
- VA: `0x0000000140851D6C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00851D8B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00851D93` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [CmpWaitForLateUnloadWorker](../../text/45/CmpWaitForLateUnloadWorker_function_004573F8.md) at `0x00457418`
- [CmpWaitForLateUnloadWorker](../../text/45/CmpWaitForLateUnloadWorker_function_004573F8.md) at `0x0045748C`
- [CmpDoQueueLateUnloadWorker](../84/CmpDoQueueLateUnloadWorker_function_0084FB18.md) at `0x0084FB55`
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x008507BF`
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00851109`
- [sub_00851966](Unknown_function_00851966.md) at `0x008519D9`
- [CmpCloseKeyObject](../86/CmpCloseKeyObject_function_00863AD0.md) at `0x00863C71`
- [sub_0086560A](../86/Unknown_function_0086560A.md) at `0x00865881`
- [sub_00865C6D](../86/Unknown_function_00865C6D.md) at `0x00865C70`
- [sub_008C7398](../8C/Unknown_function_008C7398.md) at `0x008C73B0`
- [CmpFlushNotify](../9B/CmpFlushNotify_function_009B36A8.md) at `0x009B374E`
- [CmpFlushNotify](../9B/CmpFlushNotify_function_009B36A8.md) at `0x009B377B`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCCBA`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCCD7`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCCE1`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCE50`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCE6D`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCE77`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00851D8B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00851D93` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00851D6C  40 53                           push rbx
00851D6E  48 83 EC 20                     sub rsp, 0x20
00851D72  48 8D 99 90 06 00 00            lea rbx, [rcx + 0x690]
00851D79  48 83 C8 FF                     or rax, 0xffffffffffffffff
00851D7D  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
00851D82  24 06                           and al, 6
00851D84  3C 02                           cmp al, 2
00851D86  75 08                           jne 0x140851d90
00851D88  48 8B CB                        mov rcx, rbx
00851D8B  E8 40 40 A1 FF                  call 0x140265dd0
00851D90  48 8B CB                        mov rcx, rbx
00851D93  E8 68 F8 A8 FF                  call 0x1402e1600
00851D98  48 83 C4 20                     add rsp, 0x20
00851D9C  5B                              pop rbx
00851D9D  C3                              ret
00851D9E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmUnlockHive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 1680;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 1680, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmUnlockHive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 1680;
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 + 1680, a2, a3, a4);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00851D6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00851D6C[BB_00851D6C]
  bb_00851D88[BB_00851D88]
  bb_00851D90[BB_00851D90]
  bb_00851D9E[BB_00851D9E]
  bb_00851D6C -->|branch| bb_00851D90
  bb_00851D6C -->|fallthrough| bb_00851D88
  bb_00851D88 -->|flow| bb_00851D90
```
