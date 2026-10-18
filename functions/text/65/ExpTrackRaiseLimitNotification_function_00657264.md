# ExpTrackRaiseLimitNotification

- RVA: `0x00657264`–`0x006572C8` (길이 `100` bytes)
- VA: `0x0000000140657264`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00657283` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x006572BC` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [ExpTrackTableGetMoreLimit](../2E/ExpTrackTableGetMoreLimit_function_002ECE40.md) at `0x002ECED0`
- [ExpLimitDpcInsertEntry](ExpLimitDpcInsertEntry_function_00656940.md) at `0x00656A57`
- [ExpLimitDpcInsertEntry](ExpLimitDpcInsertEntry_function_00656940.md) at `0x00656BAF`

### Static image references
- `0x0065727C` → RVA `0x00E29120` (`.data`; read)
- `0x0065728A` → RVA `0x00E29130` (`.data`; read)
- `0x00657294` → RVA `0x00E29150` (`.data`; read/write)
- `0x0065729C` → RVA `0x00657170` (`ExpPlProcessNotifications`; read)
- `0x006572A3` → RVA `0x00E29138` (`.data`; read/write)
- `0x006572AE` → RVA `0x00E29138` (`.data`; read)
- `0x006572B5` → RVA `0x00E29148` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00657264  40 53                           push rbx
00657266  48 83 EC 20                     sub rsp, 0x20
0065726A  BB 01 00 00 00                  mov ebx, 1
0065726F  33 C0                           xor eax, eax
00657271  F0 0F B1 59 60                  lock cmpxchg dword ptr [rcx + 0x60], ebx
00657276  75 49                           jne 0x1406572c1
00657278  48 8D 51 50                     lea rdx, [rcx + 0x50]
0065727C  48 8D 0D 9D 1E 7D 00            lea rcx, [rip + 0x7d1e9d]
00657283  E8 28 33 06 00                  call 0x1406ba5b0
00657288  33 C0                           xor eax, eax
0065728A  F0 0F B1 1D 9E 1E 7D 00         lock cmpxchg dword ptr [rip + 0x7d1e9e], ebx
00657292  75 2D                           jne 0x1406572c1
00657294  48 83 25 B4 1E 7D 00 00         and qword ptr [rip + 0x7d1eb4], 0
0065729C  48 8D 05 CD FE FF FF            lea rax, [rip - 0x133]
006572A3  48 83 25 8D 1E 7D 00 00         and qword ptr [rip + 0x7d1e8d], 0
006572AB  8D 53 02                        lea edx, [rbx + 2]
006572AE  48 8D 0D 83 1E 7D 00            lea rcx, [rip + 0x7d1e83]
006572B5  48 89 05 8C 1E 7D 00            mov qword ptr [rip + 0x7d1e8c], rax
006572BC  E8 5F 22 CA FF                  call 0x1402f9520
006572C1  48 83 C4 20                     add rsp, 0x20
006572C5  5B                              pop rbx
006572C6  C3                              ret
006572C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTrackRaiseLimitNotification(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 0;
    if (condition_is_not_equal) goto loc_006572C1;
    result = ExpInterlockedPushEntrySList(v_rip + 8199837, a1 + 80, a3, a4);
    result = 0;
    if (!(condition_is_not_equal)) {
        result = v_rip - 307;
        a2 = 1 + 2;
        a1 = v_rip + 8199811;
        *(unsigned __int64 *)(v_rip + 8199820) = result;
        result = ExQueueWorkItem(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpTrackRaiseLimitNotification(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 0;
    if (condition_is_not_equal) goto loc_006572C1;
    result = ExpInterlockedPushEntrySList(v_rip + 8199837, Arg1 + 80, a3, a4);
    result = 0;
    if (!(condition_is_not_equal)) {
        result = v_rip - 307;
        a2 = 1 + 2;
        Arg1 = v_rip + 8199811;
        *(uint64_t *)(v_rip + 0x7D1E8C) = result;
        result = ExQueueWorkItem(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00657264&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00657264[BB_00657264]
  bb_00657278[BB_00657278]
  bb_00657294[BB_00657294]
  bb_006572C1[BB_006572C1]
  bb_006572C7[BB_006572C7]
  bb_00657264 -->|branch| bb_006572C1
  bb_00657264 -->|fallthrough| bb_00657278
  bb_00657278 -->|branch| bb_006572C1
  bb_00657278 -->|fallthrough| bb_00657294
  bb_00657294 -->|flow| bb_006572C1
```
