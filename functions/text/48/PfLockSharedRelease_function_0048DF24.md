# PfLockSharedRelease

- RVA: `0x0048DF24`–`0x0048DF55` (길이 `49` bytes)
- VA: `0x000000014048DF24`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048DF3C` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0048DF44` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0048DF49` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [VmPinMemoryRange](../../page/7A/VmPinMemoryRange_function_007AD450.md) at `0x007AD67E`
- [VmUnpinMemoryRange](../../page/7A/VmUnpinMemoryRange_function_007AD730.md) at `0x007AD838`
- [VmpUnpinMemoryRange](../../page/7A/VmpUnpinMemoryRange_function_007ADF6C.md) at `0x007ADFC9`
- [PfCheckDeprioritizeFile](../../page/88/PfCheckDeprioritizeFile_function_00887F6C.md) at `0x00887FD5`
- [PfCheckDeprioritizeFile](../../page/88/PfCheckDeprioritizeFile_function_00887F6C.md) at `0x00888023`
- [PfCheckDeprioritizeFile](../../page/88/PfCheckDeprioritizeFile_function_00887F6C.md) at `0x00888209`
- [PfSnGetPrefetchInstructions](../../page/8A/PfSnGetPrefetchInstructions_function_008AEBE4.md) at `0x008AECD1`
- [PfSnGetPrefetchInstructions](../../page/8A/PfSnGetPrefetchInstructions_function_008AEBE4.md) at `0x008AEEE0`
- [PfSnBeginAppLaunch](../../page/95/PfSnBeginAppLaunch_function_0095EC44.md) at `0x0095EE55`
- [PfSnIsHostingApplication](../../page/95/PfSnIsHostingApplication_function_0095FF34.md) at `0x0095FF9D`
- [PfCheckDeprioritizeImage](../../page/9E/PfCheckDeprioritizeImage_function_009E97A8.md) at `0x009E97ED`
- [PfpRpCHashDeleteEntries](../../page/A3/PfpRpCHashDeleteEntries_function_00A322A8.md) at `0x00A32411`
- [sub_00B206FE](../../page/B2/Unknown_function_00B206FE.md) at `0x00B207B0`
- [sub_00B3C840](../../page/B3/Unknown_function_00B3C840.md) at `0x00B3C8D2`
- [sub_00B484E6](../../page/B4/Unknown_function_00B484E6.md) at `0x00B48879`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048DF24  40 53                           push rbx
0048DF26  48 83 EC 20                     sub rsp, 0x20
0048DF2A  48 8B D9                        mov rbx, rcx
0048DF2D  33 C9                           xor ecx, ecx
0048DF2F  8D 41 11                        lea eax, [rcx + 0x11]
0048DF32  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0048DF37  74 08                           je 0x14048df41
0048DF39  48 8B CB                        mov rcx, rbx
0048DF3C  E8 FF 54 DD FF                  call 0x140263440
0048DF41  48 8B CB                        mov rcx, rbx
0048DF44  E8 B7 36 E5 FF                  call 0x1402e1600
0048DF49  E8 62 F9 DC FF                  call 0x14025d8b0
0048DF4E  48 83 C4 20                     add rsp, 0x20
0048DF52  5B                              pop rbx
0048DF53  C3                              ret
0048DF54  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfLockSharedRelease(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = a1 + 17;
    if (!(condition_is_equal)) {
        a1 = 0;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfLockSharedRelease(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = Arg1 + 17;
    if (!(condition_is_equal)) {
        Arg1 = 0;
        result = ExfReleasePushLockShared(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1, a2, a3, a4);
    result = KeLeaveCriticalRegion(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048DF24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048DF24[BB_0048DF24]
  bb_0048DF39[BB_0048DF39]
  bb_0048DF41[BB_0048DF41]
  bb_0048DF54[BB_0048DF54]
  bb_0048DF24 -->|branch| bb_0048DF41
  bb_0048DF24 -->|fallthrough| bb_0048DF39
  bb_0048DF39 -->|flow| bb_0048DF41
```
