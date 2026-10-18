# sub_002C715F

- RVA: `0x002C715F`–`0x002C7188` (길이 `41` bytes)
- VA: `0x00000001402C715F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006ED70`
- 디코드: `8`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002C716C` → [sub_002C7096 + 0x39](Unknown_function_002C7096.md) (`tail-transfer`)
  - `0x002C7179` → [sub_002C6E36 + 0x124](Unknown_function_002C6E36.md) (`tail-transfer`)
  - `0x002C7183` → [sub_002C6E36 + 0x124](Unknown_function_002C6E36.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C715F  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002C7169  48 0B D8                        or rbx, rax
002C716C  E9 5E FF FF FF                  jmp 0x1402c70cf
002C7171  41 80 E7 05                     and r15b, 5
002C7175  41 80 FF 04                     cmp r15b, 4
002C7179  0F 85 DB FD FF FF               jne 0x1402c6f5a
002C717F  48 83 CB 42                     or rbx, 0x42
002C7183  E9 D2 FD FF FF                  jmp 0x1402c6f5a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C715F(void)
{
    __int64 v_rbx;

    v_rbx = (v_rbx) | (result);
}
```

## 5. (Beta) C Style

```c
void sub_002C715F(void)
{
    int64_t local_rbx;

    local_rbx = (local_rbx) | (result);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C715F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C715F[BB_002C715F]
  bb_002C7171[BB_002C7171]
  bb_002C717F[BB_002C717F]
  bb_002C7171 -->|fallthrough| bb_002C717F
```
