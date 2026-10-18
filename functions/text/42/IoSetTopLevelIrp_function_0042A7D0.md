# IoSetTopLevelIrp

- RVA: `0x0042A7D0`–`0x0042A7E2` (길이 `18` bytes)
- VA: `0x000000014042A7D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [FsRtlMdlReadDev](../../page/71/FsRtlMdlReadDev_function_00713980.md) at `0x00713ABA`
- [FsRtlMdlReadDev](../../page/71/FsRtlMdlReadDev_function_00713980.md) at `0x00713AFB`
- [FsRtlPrepareMdlWriteDev](../../page/71/FsRtlPrepareMdlWriteDev_function_00713BB0.md) at `0x00713E1E`
- [FsRtlPrepareMdlWriteDev](../../page/71/FsRtlPrepareMdlWriteDev_function_00713BB0.md) at `0x00713E9A`
- [sub_009848DC](../../page/98/Unknown_function_009848DC.md) at `0x00984A0B`
- [MiShareExistingControlArea](../../page/98/MiShareExistingControlArea_function_00984FAC.md) at `0x00985023`
- [MiShareExistingControlArea](../../page/98/MiShareExistingControlArea_function_00984FAC.md) at `0x00985084`
- [MiShareExistingControlArea](../../page/98/MiShareExistingControlArea_function_00984FAC.md) at `0x00985133`
- [MiCreateNewSection](../../page/98/MiCreateNewSection_function_00985DB0.md) at `0x00985F77`
- [MiCreateNewSection](../../page/98/MiCreateNewSection_function_00985DB0.md) at `0x00986258`
- [MiCreateNewSection](../../page/98/MiCreateNewSection_function_00985DB0.md) at `0x0098629D`
- [MiCreateNewSection](../../page/98/MiCreateNewSection_function_00985DB0.md) at `0x009862C3`
- [FsRtlCopyRead](../../page/A3/FsRtlCopyRead_function_00A305D0.md) at `0x00A30699`
- [FsRtlCopyRead](../../page/A3/FsRtlCopyRead_function_00A305D0.md) at `0x00A30703`
- [FsRtlCopyWrite](../../page/A4/FsRtlCopyWrite_function_00A48210.md) at `0x00A483AC`
- [FsRtlCopyWrite](../../page/A4/FsRtlCopyWrite_function_00A48210.md) at `0x00A4843B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0042A7D0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0042A7D9  48 89 88 50 05 00 00            mov qword ptr [rax + 0x550], rcx
0042A7E0  C3                              ret
0042A7E1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetTopLevelIrp(__int64 a1)
{
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1360) = a1;
    return *(unsigned __int64 *)(gs_base + (0 + 392));
}
```

## 5. (Beta) C Style

```c
int64_t IoSetTopLevelIrp(int64_t Arg1)
{
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x550) = Arg1;
    return *(uint64_t *)(gs_base + (0 + 0x188));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042A7D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042A7D0[BB_0042A7D0]
  bb_0042A7E1[BB_0042A7E1]
```
