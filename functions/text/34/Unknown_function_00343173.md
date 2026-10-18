# sub_00343173

- RVA: `0x00343173`–`0x00343196` (길이 `35` bytes)
- VA: `0x0000000140343173`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077AA4`
- 디코드: `9`개 명령, `35/35` bytes 표시
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
  - `0x00343189` → [sub_0034310B](Unknown_function_0034310B.md) (`tail-transfer`)
  - `0x0034318F` → [sub_0034310B + 0x54](Unknown_function_0034310B.md) (`tail-transfer`)
  - `0x00343191` → [sub_0034310B](Unknown_function_0034310B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00343173  48 8B 93 98 01 00 00            mov rdx, qword ptr [rbx + 0x198]
0034317A  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0034317F  48 8B 0A                        mov rcx, qword ptr [rdx]
00343182  48 C1 E9 04                     shr rcx, 4
00343186  48 3B CF                        cmp rcx, rdi
00343189  75 80                           jne 0x14034310b
0034318B  4C 39 72 08                     cmp qword ptr [rdx + 8], r14
0034318F  74 CE                           je 0x14034315f
00343191  E9 75 FF FF FF                  jmp 0x14034310b
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00343173(void)
{
    unsigned __int64 v_stack_p50;

    v_stack_p50 = *(unsigned __int64 *)(v_rbx + 408);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 408))) >> (4);
}
```

## 5. (Beta) C Style

```c
void sub_00343173(void)
{
    uint64_t v_stack_p50;

    v_stack_p50 = *(uint64_t *)(local_rbx + 0x198);
    a1 = (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x198))) >> (4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00343173&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00343173[BB_00343173]
  bb_0034318B[BB_0034318B]
  bb_00343191[BB_00343191]
  bb_00343173 -->|fallthrough| bb_0034318B
  bb_0034318B -->|fallthrough| bb_00343191
```
