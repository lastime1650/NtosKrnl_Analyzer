# sub_0024D9D1

- RVA: `0x0024D9D1`–`0x0024D9E9` (길이 `24` bytes)
- VA: `0x000000014024D9D1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062EA4`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0024D9DB` → [MiLocatePagefileSubsection](../36/MiLocatePagefileSubsection_function_00367AC0.md) (function, `0x00367AC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0024D9E3` → [sub_0024D9A3 + 0x16](Unknown_function_0024D9A3.md) (`tail-transfer`)
  - `0x0024D9E7` → [sub_0024D9A3](Unknown_function_0024D9A3.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024D9D1  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
0024D9D8  49 8B D6                        mov rdx, r14
0024D9DB  E8 E0 A0 11 00                  call 0x140367ac0
0024D9E0  48 8B D8                        mov rbx, rax
0024D9E3  EB D4                           jmp 0x14024d9b9
0024D9E5  33 DB                           xor ebx, ebx
0024D9E7  EB BA                           jmp 0x14024d9a3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024D9D1(void)
{
    __int64 result;

    result = MiLocatePagefileSubsection(v_rdi + 128, v_r14, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0024D9D1(void)
{
    int64_t result;

    result = MiLocatePagefileSubsection(local_rdi + 128, local_r14, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024D9D1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024D9D1[BB_0024D9D1]
  bb_0024D9E5[BB_0024D9E5]
```
