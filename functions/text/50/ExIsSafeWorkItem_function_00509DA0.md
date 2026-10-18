# ExIsSafeWorkItem

- RVA: `0x00509DA0`–`0x00509DB1` (길이 `17` bytes)
- VA: `0x0000000140509DA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwTraceThreadWorkItem](../4D/EtwTraceThreadWorkItem_function_004DC3D0.md) at `0x004DC3F9`

### Static image references
- `0x00509DA2` → RVA `0x0050A560` (`.text`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00509DA0  33 C0                           xor eax, eax
00509DA2  48 8D 15 B7 07 00 00            lea rdx, [rip + 0x7b7]
00509DA9  48 3B CA                        cmp rcx, rdx
00509DAC  0F 94 C0                        sete al
00509DAF  C3                              ret
00509DB0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExIsSafeWorkItem(__int64 a1)
{
    __int64 result;

    result = 0;
    result = (a1 == (v_rip + 1975)) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExIsSafeWorkItem(int64_t Arg1)
{
    int64_t result;

    result = 0;
    result = (Arg1 == (v_rip + 1975)) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00509DA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00509DA0[BB_00509DA0]
  bb_00509DB0[BB_00509DB0]
```
