# KiSetUserTbFlushPending

- RVA: `0x006B20C0`–`0x006B20CA` (길이 `10` bytes)
- VA: `0x00000001406B20C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C174C`
- 디코드: `2`개 명령, `10/10` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiFlushEntireTbDueToAttributeChange](../30/MiFlushEntireTbDueToAttributeChange_function_00308AE0.md) at `0x00308C2A`
- [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) at `0x003092A6`
- [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) at `0x003092CF`
- [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) at `0x00309321`
- [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) at `0x00309397`
- [KiFlushRangeWorker](../31/KiFlushRangeWorker_function_00311A70.md) at `0x00311BB9`
- [KiFlushRangeWorker](../31/KiFlushRangeWorker_function_00311A70.md) at `0x00311BC3`
- [sub_00312A48](../31/Unknown_function_00312A48.md) at `0x00312A48`
- [sub_00312A48](../31/Unknown_function_00312A48.md) at `0x00312A57`
- [sub_00314608](../31/Unknown_function_00314608.md) at `0x0031462B`
- [sub_003A3F33](../3A/Unknown_function_003A3F33.md) at `0x003A3F5A`
- [sub_003A3F33](../3A/Unknown_function_003A3F33.md) at `0x003A3F8B`
- [sub_003A3F33](../3A/Unknown_function_003A3F33.md) at `0x003A3FA9`
- [KiFlushRangeTb](../40/KiFlushRangeTb_function_00401D40.md) at `0x00401E5A`
- [KiFlushRangeTb](../40/KiFlushRangeTb_function_00401D40.md) at `0x00401E64`
- [KiFlushCurrentTbOnly](../44/KiFlushCurrentTbOnly_function_00448080.md) at `0x004480E7`
- [KeDeepSleepProcessor](../5B/KeDeepSleepProcessor_function_005BDB24.md) at `0x005BDBA9`
- [KeFlushSingleCurrentTb](../5B/KeFlushSingleCurrentTb_function_005BDC9C.md) at `0x005BDDC7`
- [KeFlushSingleTb](../5B/KeFlushSingleTb_function_005BDE84.md) at `0x005BDF1F`
- [KiFlushSingleTbWorker](../5C/KiFlushSingleTbWorker_function_005CAD90.md) at `0x005CADF6`
- [sub_006E6498](../6E/Unknown_function_006E6498.md) at `0x006E64F7`
- [KiInitializeKernel](../../pagelk/B6/KiInitializeKernel_function_00B68D20.md) at `0x00B68E66`
- [KiInitializeKernel](../../pagelk/B6/KiInitializeKernel_function_00B68D20.md) at `0x00B68EFB`
- [KeWriteProtectPAT](../../pagelk/B6/KeWriteProtectPAT_function_00B6ABD0.md) at `0x00B6AC78`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006B20C0  65 83 0C 25 18 B0 00 00 01      or dword ptr gs:[0xb018], 1
006B20C9  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiSetUserTbFlushPending(void)
{
    return;
}
```

## 5. (Beta) C Style

```c
void KiSetUserTbFlushPending(void)
{
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B20C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B20C0[BB_006B20C0]
```
