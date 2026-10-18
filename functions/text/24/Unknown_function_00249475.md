# sub_00249475

- RVA: `0x00249475`–`0x0024948A` (길이 `21` bytes)
- VA: `0x0000000140249475`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000627FC`
- 디코드: `5`개 명령, `21/21` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00249481` → [sub_00249538](Unknown_function_00249538.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00249475  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0024947A  8B 5F 20                        mov ebx, dword ptr [rdi + 0x20]
0024947D  0F BA E3 13                     bt ebx, 0x13
00249481  0F 83 B1 00 00 00               jae 0x140249538
00249487  48 8B 07                        mov rax, qword ptr [rdi]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00249475(void)
{
    unsigned __int64 v_stack_p50;

    v_stack_p50 = v_rbx;
    return *(unsigned __int64 *)(v_rdi);
}
```

## 5. (Beta) C Style

```c
void sub_00249475(void)
{
    uint64_t v_stack_p50;

    v_stack_p50 = local_rbx;
    return *(uint64_t *)(local_rdi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00249475&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00249475[BB_00249475]
  bb_00249487[BB_00249487]
  bb_00249475 -->|fallthrough| bb_00249487
```
