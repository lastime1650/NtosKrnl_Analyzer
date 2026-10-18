# sub_008E4495

- RVA: `0x008E4495`–`0x008E44D3` (길이 `62` bytes)
- VA: `0x00000001408E4495`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000862C0`
- 디코드: `17`개 명령, `62/62` bytes 표시
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
  - `0x008E4498` → [sub_008E41B3 + 0x17A](Unknown_function_008E41B3.md) (`tail-transfer`)
  - `0x008E44A1` → [sub_008E41B3 + 0x17A](Unknown_function_008E41B3.md) (`tail-transfer`)
  - `0x008E44CE` → [sub_008E41B3 + 0x17A](Unknown_function_008E41B3.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E4495  48 85 DB                        test rbx, rbx
008E4498  0F 84 8F FE FF FF               je 0x1408e432d
008E449E  66 3B C7                        cmp ax, di
008E44A1  0F 82 86 FE FF FF               jb 0x1408e432d
008E44A7  48 8B C8                        mov rcx, rax
008E44AA  44 8B C0                        mov r8d, eax
008E44AD  48 C1 E9 08                     shr rcx, 8
008E44B1  41 83 E0 0F                     and r8d, 0xf
008E44B5  0F B7 14 4B                     movzx edx, word ptr [rbx + rcx*2]
008E44B9  8B C8                           mov ecx, eax
008E44BB  C1 E9 04                        shr ecx, 4
008E44BE  83 E1 0F                        and ecx, 0xf
008E44C1  03 D1                           add edx, ecx
008E44C3  0F B7 14 53                     movzx edx, word ptr [rbx + rdx*2]
008E44C7  41 03 D0                        add edx, r8d
008E44CA  66 03 04 53                     add ax, word ptr [rbx + rdx*2]
008E44CE  E9 5A FE FF FF                  jmp 0x1408e432d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008E4495(void)
{
    __int64 result;

    a1 = (result) >> (8);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (15));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (4));
    a1 = (unsigned int)((a1) & (15));
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rbx + a1 * 2)) + ((unsigned int)(a1)));
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rbx + a2 * 2)) + ((unsigned int)(a3)));
    result = (unsigned __int16)((result) + (*(unsigned __int16 *)(v_rbx + a2 * 2)));
}
```

## 5. (Beta) C Style

```c
void sub_008E4495(void)
{
    int64_t result;

    a1 = (result) >> (8);
    a3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (15));
    a1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (4));
    a1 = (uint32_t)((a1) & (15));
    a2 = (uint32_t)((*(uint16_t *)(local_rbx + a1 * 2)) + ((uint32_t)(a1)));
    a2 = (uint32_t)((*(uint16_t *)(local_rbx + a2 * 2)) + ((uint32_t)(a3)));
    result = (uint16_t)((result) + (*(uint16_t *)(local_rbx + a2 * 2)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E4495&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E4495[BB_008E4495]
  bb_008E449E[BB_008E449E]
  bb_008E44A7[BB_008E44A7]
  bb_008E4495 -->|fallthrough| bb_008E449E
  bb_008E449E -->|fallthrough| bb_008E44A7
```
