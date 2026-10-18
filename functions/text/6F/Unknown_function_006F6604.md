# sub_006F6604

- RVA: `0x006F6604`–`0x006F661F` (길이 `27` bytes)
- VA: `0x00000001406F6604`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B13A4`
- 디코드: `7`개 명령, `27/27` bytes 표시
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
  - `0x006F661A` → [GxpAdjustRectangleToFrameBuffer + 0x158](../48/GxpAdjustRectangleToFrameBuffer_function_0048CDC8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F6604  41 8B D4                        mov edx, r12d
006F6607  41 2B 16                        sub edx, dword ptr [r14]
006F660A  41 2B D3                        sub edx, r11d
006F660D  89 54 24 0C                     mov dword ptr [rsp + 0xc], edx
006F6611  45 8B 46 04                     mov r8d, dword ptr [r14 + 4]
006F6615  44 89 44 24 08                  mov dword ptr [rsp + 8], r8d
006F661A  E9 01 69 D9 FF                  jmp 0x14048cf20
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006F6604(void)
{
    unsigned int v_stack_p8;
    unsigned int v_stack_pC;

    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - (*(unsigned int *)(v_r14)));
    a2 = (unsigned int)((a2) - ((unsigned int)(v_r11)));
    v_stack_pC = (unsigned int)(a2);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)));
}
```

## 5. (Beta) C Style

```c
void sub_006F6604(void)
{
    uint32_t v_stack_p8;
    uint32_t v_stack_pC;

    a2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - (*(uint32_t *)(local_r14)));
    a2 = (uint32_t)((a2) - ((uint32_t)(local_r11)));
    v_stack_pC = (uint32_t)(a2);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F6604&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F6604[BB_006F6604]
```
