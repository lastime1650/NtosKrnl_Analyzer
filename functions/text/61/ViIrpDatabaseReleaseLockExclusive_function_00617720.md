# ViIrpDatabaseReleaseLockExclusive

- RVA: `0x00617720`–`0x00617738` (길이 `24` bytes)
- VA: `0x0000000140617720`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0061772D` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)

### Direct callers
- [ViPendingCompleteAfterWait](../../pagevrfy/BA/ViPendingCompleteAfterWait_function_00BA1D18.md) at `0x00BA1DDB`
- [VfIrpDatabaseEntryInsertAndLock](../../pagevrfy/BB/VfIrpDatabaseEntryInsertAndLock_function_00BB3F00.md) at `0x00BB3FA7`
- [VfIrpDatabaseEntryReleaseLock](../../pagevrfy/BB/VfIrpDatabaseEntryReleaseLock_function_00BB3FD4.md) at `0x00BB403D`
- [VfIrpDatabaseEntryReleaseLock](../../pagevrfy/BB/VfIrpDatabaseEntryReleaseLock_function_00BB3FD4.md) at `0x00BB40AA`
- [sub_00BBBE00](../../pagevrfy/BB/Unknown_function_00BBBE00.md) at `0x00BBC049`
- [sub_00BBC0C8](../../pagevrfy/BB/Unknown_function_00BBC0C8.md) at `0x00BBC158`
- [sub_00BBC0C8](../../pagevrfy/BB/Unknown_function_00BBC0C8.md) at `0x00BBC1E6`
- [sub_00BBC208](../../pagevrfy/BB/Unknown_function_00BBC208.md) at `0x00BBC29C`

### Static image references
- `0x00617726` → RVA `0x00F04888` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00617720  48 83 EC 28                     sub rsp, 0x28
00617724  8A D1                           mov dl, cl
00617726  48 8D 0D 5B D1 8E 00            lea rcx, [rip + 0x8ed15b]
0061772D  E8 BE 97 CA FF                  call 0x1402c0ef0
00617732  48 83 C4 28                     add rsp, 0x28
00617736  C3                              ret
00617737  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIrpDatabaseReleaseLockExclusive(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExReleaseSpinLockExclusive(v_rip + 9359707, a1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIrpDatabaseReleaseLockExclusive(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExReleaseSpinLockExclusive(v_rip + 9359707, Arg1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00617720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00617720[BB_00617720]
  bb_00617737[BB_00617737]
```
