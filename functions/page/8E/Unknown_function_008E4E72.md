# sub_008E4E72

- RVA: `0x008E4E72`–`0x008E4E83` (길이 `17` bytes)
- VA: `0x00000001408E4E72`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000864E4`
- 디코드: `4`개 명령, `17/17` bytes 표시
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
- `0x008E4E77` → RVA `0x00F8B880` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008E4E75` → [sub_008E4ECA](Unknown_function_008E4ECA.md) (`tail-transfer`)
  - `0x008E4E7E` → [sub_008E4A5E + 0x1C](Unknown_function_008E4A5E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E4E72  83 E9 01                        sub ecx, 1
008E4E75  75 53                           jne 0x1408e4eca
008E4E77  48 8D 3D 02 6A 6A 00            lea rdi, [rip + 0x6a6a02]
008E4E7E  E9 F7 FB FF FF                  jmp 0x1408e4a7a
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_008E4E72(int a1)
{
    a1 = (unsigned int)((a1) - (1));
}
```

## 5. (Beta) C Style

```c
void sub_008E4E72(int32_t Arg1)
{
    Arg1 = (uint32_t)((Arg1) - (1));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E4E72&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E4E72[BB_008E4E72]
  bb_008E4E77[BB_008E4E77]
  bb_008E4E72 -->|fallthrough| bb_008E4E77
```
