# sub_006D8C66

- RVA: `0x006D8C66`–`0x006D8CA4` (길이 `62` bytes)
- VA: `0x00000001406D8C66`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000638FC`
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006D8C9F` → [KiEnumerateNextSchedulerSubNodeInSystem + 0xDB](../25/KiEnumerateNextSchedulerSubNodeInSystem_function_002569C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D8C66  0F B6 10                        movzx edx, byte ptr [rax]
006D8C69  48 8D 40 01                     lea rax, [rax + 1]
006D8C6D  41 8B C8                        mov ecx, r8d
006D8C70  48 3B CB                        cmp rcx, rbx
006D8C73  75 0D                           jne 0x1406d8c82
006D8C75  4D 85 E4                        test r12, r12
006D8C78  74 08                           je 0x1406d8c82
006D8C7A  43 22 94 1C 90 C8 02 00         and dl, byte ptr [r12 + r11 + 0x2c890]
006D8C82  0F B6 CA                        movzx ecx, dl
006D8C85  41 FF C0                        inc r8d
006D8C88  F7 D1                           not ecx
006D8C8A  0F B6 D1                        movzx edx, cl
006D8C8D  42 0F B6 8C 1A 40 41 03 00      movzx ecx, byte ptr [rdx + r11 + 0x34140]
006D8C96  4C 03 D1                        add r10, rcx
006D8C99  41 83 C7 FF                     add r15d, -1
006D8C9D  75 C7                           jne 0x1406d8c66
006D8C9F  E9 F7 DD B7 FF                  jmp 0x140256a9b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D8C66(__int64 a1, __int64 a2, int a3)
{
    __int64 v_r10;
    __int64 v_r15;

    if (((unsigned int)(a3)) != v_rbx) goto loc_006D8C82;
    if (v_r12 != 0) {
        a2 = (unsigned __int8)((*(unsigned __int8 *)(result)) & (*(unsigned __int8 *)(v_r12 + v_r11 * 1 + 182416)));
    }
    a3 = (unsigned int)((a3) + 1);
    a1 = (unsigned int)(~((unsigned __int8)(a2)));
    v_r10 = (v_r10) + (*(unsigned __int8 *)((unsigned __int8)(a1) + v_r11 * 1 + 213312));
    v_r15 = (unsigned int)((v_r15) + (-1));
    if (condition_is_not_equal) goto loc_006D8C66;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D8C66(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t local_r10;
    int64_t local_r15;

    if (((uint32_t)(Arg3)) != local_rbx) goto loc_006D8C82;
    if (local_r12 != 0) {
        Arg2 = (uint8_t)((*(uint8_t *)(result)) & (*(uint8_t *)(local_r12 + local_r11 * 1 + 0x2C890)));
    }
    Arg3 = (uint32_t)((Arg3) + 1);
    Arg1 = (uint32_t)(~((uint8_t)(Arg2)));
    local_r10 = (local_r10) + (*(uint8_t *)((uint8_t)(Arg1) + local_r11 * 1 + 0x34140));
    local_r15 = (uint32_t)((local_r15) + (-1));
    if (condition_is_not_equal) goto loc_006D8C66;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D8C66&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D8C66[BB_006D8C66]
  bb_006D8C75[BB_006D8C75]
  bb_006D8C7A[BB_006D8C7A]
  bb_006D8C82[BB_006D8C82]
  bb_006D8C9F[BB_006D8C9F]
  bb_006D8C66 -->|branch| bb_006D8C82
  bb_006D8C66 -->|fallthrough| bb_006D8C75
  bb_006D8C75 -->|branch| bb_006D8C82
  bb_006D8C75 -->|fallthrough| bb_006D8C7A
  bb_006D8C7A -->|flow| bb_006D8C82
  bb_006D8C82 -->|branch| bb_006D8C66
  bb_006D8C82 -->|fallthrough| bb_006D8C9F
```
