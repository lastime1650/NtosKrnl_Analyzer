# ExpReleasePoolListLockExclusive

- RVA: `0x0065D868`–`0x0065D8A2` (길이 `58` bytes)
- VA: `0x000000014065D868`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0065D886` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0065D892` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0065D897` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [ExpPrivatePoolCreate](../../page/7D/ExpPrivatePoolCreate_function_007D5F98.md) at `0x007D6185`
- [ExpPrivatePoolDestroy](../../page/7D/ExpPrivatePoolDestroy_function_007D61C4.md) at `0x007D6202`

### Static image references
- `0x0065D870` → RVA `0x00E6BEE0` (`.data`; read/write)
- `0x0065D87F` → RVA `0x00E6BEE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065D868  48 83 EC 28                     sub rsp, 0x28
0065D86C  48 83 C8 FF                     or rax, 0xffffffffffffffff
0065D870  F0 48 0F C1 05 67 E6 80 00      lock xadd qword ptr [rip + 0x80e667], rax
0065D879  24 06                           and al, 6
0065D87B  3C 02                           cmp al, 2
0065D87D  75 0C                           jne 0x14065d88b
0065D87F  48 8D 0D 5A E6 80 00            lea rcx, [rip + 0x80e65a]
0065D886  E8 45 85 C0 FF                  call 0x140265dd0
0065D88B  48 8D 0D 4E E6 80 00            lea rcx, [rip + 0x80e64e]
0065D892  E8 69 3D C8 FF                  call 0x1402e1600
0065D897  E8 14 00 C0 FF                  call 0x14025d8b0
0065D89C  48 83 C4 28                     add rsp, 0x28
0065D8A0  C3                              ret
0065D8A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpReleasePoolListLockExclusive(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 8447578;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 8447566, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 8447566, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExpReleasePoolListLockExclusive(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        a1 = v_rip + 8447578;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 8447566, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 8447566, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065D868&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065D868[BB_0065D868]
  bb_0065D87F[BB_0065D87F]
  bb_0065D88B[BB_0065D88B]
  bb_0065D8A1[BB_0065D8A1]
  bb_0065D868 -->|branch| bb_0065D88B
  bb_0065D868 -->|fallthrough| bb_0065D87F
  bb_0065D87F -->|flow| bb_0065D88B
```
