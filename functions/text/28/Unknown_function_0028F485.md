# sub_0028F485

- RVA: `0x0028F485`–`0x0028F4C4` (길이 `63` bytes)
- VA: `0x000000014028F485`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067290`
- 디코드: `16`개 명령, `63/63` bytes 표시
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
  - `0x0028F4BE` → [sub_0028F57A + 0x4A](Unknown_function_0028F57A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0028F485  8B 8E B8 00 00 00               mov ecx, dword ptr [rsi + 0xb8]
0028F48B  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0028F48F  C1 E9 08                        shr ecx, 8
0028F492  0F B6 C1                        movzx eax, cl
0028F495  80 E1 0F                        and cl, 0xf
0028F498  C0 E8 04                        shr al, 4
0028F49B  FE C8                           dec al
0028F49D  C0 E0 04                        shl al, 4
0028F4A0  0A C1                           or al, cl
0028F4A2  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0028F4A6  0F B7 44 24 30                  movzx eax, word ptr [rsp + 0x30]
0028F4AB  66 89 86 B8 00 00 00            mov word ptr [rsi + 0xb8], ax
0028F4B2  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0028F4B6  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0028F4BB  48 85 C9                        test rcx, rcx
0028F4BE  0F 85 00 01 00 00               jne 0x14028f5c4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0028F485(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int16 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p31;

    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 184)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 184))) >> (8));
    a1 = (unsigned __int8)((a1) & (15));
    result = (unsigned __int8)(((unsigned __int8)(a1)) >> (4));
    result = (unsigned __int8)((result) - 1);
    result = (unsigned __int8)((result) << (4));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    v_stack_p31 = (unsigned __int8)(result);
    *(unsigned __int16 *)(v_rsi + 184) = a6;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0028F485(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint16_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t result;
    uint32_t v_stack_p30;
    uint8_t v_stack_p31;

    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0xB8)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) & (15));
    result = (uint8_t)(((uint8_t)(Arg1)) >> (4));
    result = (uint8_t)((result) - 1);
    result = (uint8_t)((result) << (4));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    v_stack_p31 = (uint8_t)(result);
    *(uint16_t *)(local_rsi + 0xB8) = Arg6;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0028F485&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0028F485[BB_0028F485]
```
