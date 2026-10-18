# KeQueryTimeIncrement

- RVA: `0x0044B4C0`–`0x0044B4C8` (길이 `8` bytes)
- VA: `0x000000014044B4C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `8/8` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00703B14](../../page/70/Unknown_function_00703B14.md) at `0x00703BF7`
- [sub_007C7FB0](../../page/7C/Unknown_function_007C7FB0.md) at `0x007C80B8`
- [sub_007C7FB0](../../page/7C/Unknown_function_007C7FB0.md) at `0x007C827D`
- [EtwpSendDataBlock](../../page/8C/EtwpSendDataBlock_function_008C8530.md) at `0x008C864C`
- [SPCallServerHandleQueryPolicy](../../page/96/SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096B363`
- [FsRtlCancellableWaitForMultipleObjects](../../page/9F/FsRtlCancellableWaitForMultipleObjects_function_009F1EE0.md) at `0x009F1F23`
- [FsRtlCancellableWaitForMultipleObjects](../../page/9F/FsRtlCancellableWaitForMultipleObjects_function_009F1EE0.md) at `0x009F1FE4`
- [FsRtlCancellableWaitForSingleObject](../../page/A1/FsRtlCancellableWaitForSingleObject_function_00A1D890.md) at `0x00A1D8CD`
- [FsRtlCancellableWaitForSingleObject](../../page/A1/FsRtlCancellableWaitForSingleObject_function_00A1D890.md) at `0x00A1D947`
- [sub_00B28806](../../page/B2/Unknown_function_00B28806.md) at `0x00B2881B`
- [sub_00C6D0F8](../../init/C6/Unknown_function_00C6D0F8.md) at `0x00C6D14A`

### Static image references
- `0x0044B4C0` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044B4C0  8B 05 DA B5 B7 00               mov eax, dword ptr [rip + 0xb7b5da]
0044B4C6  C3                              ret
0044B4C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryTimeIncrement(void)
{
    return (unsigned int)(*(unsigned int *)(v_rip + 12039642));
}
```

## 5. (Beta) C Style

```c
void KeQueryTimeIncrement(void)
{
    return (uint32_t)(*(uint32_t *)(v_rip + 0xB7B5DA));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044B4C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044B4C0[BB_0044B4C0]
  bb_0044B4C7[BB_0044B4C7]
```
