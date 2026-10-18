# sub_008E40F7

- RVA: `0x008E40F7`–`0x008E4109` (길이 `18` bytes)
- VA: `0x00000001408E40F7`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086200`
- 디코드: `4`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008E40FF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008E40FF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008E40FA` → [sub_008E3F77 + 0x16](Unknown_function_008E3F77.md) (`tail-transfer`)
  - `0x008E4104` → [sub_008E3F77 + 0x3B](Unknown_function_008E3F77.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E40F7  45 33 F6                        xor r14d, r14d
008E40FA  E9 8E FE FF FF                  jmp 0x1408e3f8d
008E40FF  E8 CC 69 DD FF                  call 0x1406baad0
008E4104  E9 A9 FE FF FF                  jmp 0x1408e3fb2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008E40F7(void)
{
    __int64 v_r14;

    v_r14 = 0;
}
```

## 5. (Beta) C Style

```c
void sub_008E40F7(void)
{
    int64_t local_r14;

    local_r14 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E40F7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E40F7[BB_008E40F7]
  bb_008E40FF[BB_008E40FF]
```
