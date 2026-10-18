# sub_006DC7D6

- RVA: `0x006DC7D6`–`0x006DC7ED` (길이 `23` bytes)
- VA: `0x00000001406DC7D6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EE98`
- 디코드: `5`개 명령, `23/23` bytes 표시
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
- `0x006DC7E0` → RVA `0x00E0EC64` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006DC7DB` → [AccelpSiovInternalOperationHandler + 0x61](../2C/AccelpSiovInternalOperationHandler_function_002C7DDC.md) (`tail-transfer`)
  - `0x006DC7E8` → [AccelpSiovInternalOperationHandler + 0xD5](../2C/AccelpSiovInternalOperationHandler_function_002C7DDC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DC7D6  BF BB 00 00 C0                  mov edi, 0xc00000bb
006DC7DB  E9 5D B6 BE FF                  jmp 0x1402c7e3d
006DC7E0  89 3D 7E 24 73 00               mov dword ptr [rip + 0x73247e], edi
006DC7E6  8B D7                           mov edx, edi
006DC7E8  E9 C4 B6 BE FF                  jmp 0x1402c7eb1
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006DC7D6(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_006DC7D6(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DC7D6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DC7D6[BB_006DC7D6]
  bb_006DC7E0[BB_006DC7E0]
```
