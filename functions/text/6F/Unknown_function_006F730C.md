# sub_006F730C

- RVA: `0x006F730C`–`0x006F731D` (길이 `17` bytes)
- VA: `0x00000001406F730C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B31FC`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F7312` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F7318` → [MiDeleteShadowStackPtes + 0x84](../49/MiDeleteShadowStackPtes_function_00493AE4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F730C  48 8B D7                        mov rdx, rdi
006F730F  48 8B CD                        mov rcx, rbp
006F7312  E8 A9 FB B1 FF                  call 0x140216ec0
006F7317  90                              nop
006F7318  E9 4B C8 D9 FF                  jmp 0x140493b68
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F730C(void)
{
    __int64 result;

    result = MiUnlockPageTable(v_rbp, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006F730C(void)
{
    int64_t result;

    result = MiUnlockPageTable(local_rbp, local_rdi, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F730C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F730C[BB_006F730C]
```
