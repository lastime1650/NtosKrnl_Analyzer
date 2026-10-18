# sub_0024382B

- RVA: `0x0024382B`–`0x00243852` (길이 `39` bytes)
- VA: `0x000000014024382B`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061C7C`
- 디코드: `9`개 명령, `39/39` bytes 표시
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
  - `0x0024384D` → [sub_00243729](Unknown_function_00243729.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024382B  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0024382F  4A 8D 14 30                     lea rdx, [rax + r14]
00243833  48 8B CA                        mov rcx, rdx
00243836  48 33 C8                        xor rcx, rax
00243839  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
00243843  48 23 C8                        and rcx, rax
00243846  48 33 CA                        xor rcx, rdx
00243849  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
0024384D  E9 D7 FE FF FF                  jmp 0x140243729
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024382B(void)
{
    a1 = (*(unsigned __int64 *)(v_rbx + 24) + v_r14 * 1) ^ (*(unsigned __int64 *)(v_rbx + 24));
    a1 = (a1) & (*(unsigned __int64 *)(v_rbx + 24));
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rbx + 24) + v_r14 * 1);
    *(unsigned __int64 *)(v_rbx + 24) = a1;
}
```

## 5. (Beta) C Style

```c
void sub_0024382B(void)
{
    a1 = (*(uint64_t *)(local_rbx + 0x18) + local_r14 * 1) ^ (*(uint64_t *)(local_rbx + 0x18));
    a1 = (a1) & (*(uint64_t *)(local_rbx + 0x18));
    a1 = (a1) ^ (*(uint64_t *)(local_rbx + 0x18) + local_r14 * 1);
    *(uint64_t *)(local_rbx + 0x18) = a1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024382B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024382B[BB_0024382B]
```
