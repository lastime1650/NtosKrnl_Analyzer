# HalpDmaCvmHandleUnrecoverableFrames

- RVA: `0x00550CEC`–`0x00550CF6` (길이 `10` bytes)
- VA: `0x0000000140550CEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `10/10` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpDmaCvmSetPageShareability](../../page/70/HalpDmaCvmSetPageShareability_function_0070973C.md) at `0x007097BE`

### Static image references
- `0x00550CEC` → RVA `0x00FC18B0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00550CEC  F0 44 01 05 BC 0B A7 00         lock add dword ptr [rip + 0xa70bbc], r8d
00550CF4  C3                              ret
00550CF5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall HalpDmaCvmHandleUnrecoverableFrames(__int64 a1, __int64 a2, int a3)
{
    return;
}
```

## 5. (Beta) C Style

```c
void HalpDmaCvmHandleUnrecoverableFrames(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00550CEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00550CEC[BB_00550CEC]
  bb_00550CF5[BB_00550CF5]
```
