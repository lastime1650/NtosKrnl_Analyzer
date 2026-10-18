# sub_006DC410

- RVA: `0x006DC410`–`0x006DC421` (길이 `17` bytes)
- VA: `0x00000001406DC410`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E9D4`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DC416` → [MiComputeAweCharges](../../page/6F/MiComputeAweCharges_function_006FE84C.md) (function, `0x006FE84C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006DC416` → [MiComputeAweCharges](../../page/6F/MiComputeAweCharges_function_006FE84C.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DC41C` → [MiComputeVadCharges + 0xF9](../2C/MiComputeVadCharges_function_002C3348.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DC410  49 8B D0                        mov rdx, r8
006DC413  49 8B C9                        mov rcx, r9
006DC416  E8 31 24 02 00                  call 0x1406fe84c
006DC41B  90                              nop
006DC41C  E9 20 70 BE FF                  jmp 0x1402c3441
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DC410(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    result = MiComputeAweCharges(a4, a3, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DC410(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;

    result = MiComputeAweCharges(Arg4, Arg3, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DC410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DC410[BB_006DC410]
```
