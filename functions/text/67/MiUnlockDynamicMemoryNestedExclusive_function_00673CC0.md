# MiUnlockDynamicMemoryNestedExclusive

- RVA: `0x00673CC0`–`0x00673CF5` (길이 `53` bytes)
- VA: `0x0000000140673CC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00673CDE` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00673CEA` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [MiReleaseAddMemoryLocks](../../page/7F/MiReleaseAddMemoryLocks_function_007FACEC.md) at `0x007FAD15`
- [MiNodeZeroConductor](../../page/81/MiNodeZeroConductor_function_00810AC0.md) at `0x00810B25`

### Static image references
- `0x00673CC8` → RVA `0x00E38DC0` (`.data`; read/write)
- `0x00673CD7` → RVA `0x00E38DC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00673CC0  48 83 EC 28                     sub rsp, 0x28
00673CC4  48 83 C8 FF                     or rax, 0xffffffffffffffff
00673CC8  F0 48 0F C1 05 EF 50 7C 00      lock xadd qword ptr [rip + 0x7c50ef], rax
00673CD1  24 06                           and al, 6
00673CD3  3C 02                           cmp al, 2
00673CD5  75 0C                           jne 0x140673ce3
00673CD7  48 8D 0D E2 50 7C 00            lea rcx, [rip + 0x7c50e2]
00673CDE  E8 ED 20 BF FF                  call 0x140265dd0
00673CE3  48 8D 0D D6 50 7C 00            lea rcx, [rip + 0x7c50d6]
00673CEA  E8 11 D9 C6 FF                  call 0x1402e1600
00673CEF  48 83 C4 28                     add rsp, 0x28
00673CF3  C3                              ret
00673CF4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockDynamicMemoryNestedExclusive(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 8147170;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 8147158, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiUnlockDynamicMemoryNestedExclusive(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        a1 = v_rip + 8147170;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 8147158, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00673CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00673CC0[BB_00673CC0]
  bb_00673CD7[BB_00673CD7]
  bb_00673CE3[BB_00673CE3]
  bb_00673CF4[BB_00673CF4]
  bb_00673CC0 -->|branch| bb_00673CE3
  bb_00673CC0 -->|fallthrough| bb_00673CD7
  bb_00673CD7 -->|flow| bb_00673CE3
```
