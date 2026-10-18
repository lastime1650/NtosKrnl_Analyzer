# sub_002C6E1D

- RVA: `0x002C6E1D`–`0x002C6E36` (길이 `25` bytes)
- VA: `0x00000001402C6E1D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006ECC4`
- 디코드: `5`개 명령, `25/25` bytes 표시
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
- `0x002C6E27` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002C6E30` → [sub_002C7057](Unknown_function_002C7057.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C6E1D  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
002C6E22  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002C6E27  4C 8D 35 D2 91 D3 FF            lea r14, [rip - 0x2c6e2e]
002C6E2E  85 F6                           test esi, esi
002C6E30  0F 84 21 02 00 00               je 0x1402c7057
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002C6E1D(void)
{
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;

    v_stack_p58 = v_rbx;
    v_stack_p68 = v_r14;
}
```

## 5. (Beta) C Style

```c
void sub_002C6E1D(void)
{
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;

    v_stack_p58 = local_rbx;
    v_stack_p68 = local_r14;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C6E1D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C6E1D[BB_002C6E1D]
```
