# IopLiveDumpTracingControlCallback

- RVA: `0x005A4520`–`0x005A452F` (길이 `15` bytes)
- VA: `0x00000001405A4520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005A4527` → RVA `0x00E66230` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A4520  33 C0                           xor eax, eax
005A4522  85 D2                           test edx, edx
005A4524  0F 95 C0                        setne al
005A4527  87 05 03 1D 8C 00               xchg dword ptr [rip + 0x8c1d03], eax
005A452D  C3                              ret
005A452E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpTracingControlCallback(__int64 a1, int a2)
{
    __int64 result;

    result = 0;
    result = (a2 != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpTracingControlCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    result = 0;
    result = (Arg2 != 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A4520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A4520[BB_005A4520]
  bb_005A452E[BB_005A452E]
```
