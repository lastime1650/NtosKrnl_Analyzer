# EtwpTiClearBloomFilter

- RVA: `0x003B92E4`–`0x003B935A` (길이 `118` bytes)
- VA: `0x00000001403B92E4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `34`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003B92FB` → [EtwpTiGetHashedBitNumbers](EtwpTiGetHashedBitNumbers_function_003B971C.md) (function, `0x003B971C`)

### Direct callers
- [EtwpTiVadQueryEventWriteCallback](../../page/A0/EtwpTiVadQueryEventWriteCallback_function_00A03970.md) at `0x00A03A26`

### Static image references
- `0x003B930D` → RVA `0x00EFF1A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B92E4  48 83 EC 38                     sub rsp, 0x38
003B92E8  33 C0                           xor eax, eax
003B92EA  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
003B92EF  4C 8B C2                        mov r8, rdx
003B92F2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003B92F7  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003B92FB  E8 1C 04 00 00                  call 0x1403b971c
003B9300  8B 4C 24 20                     mov ecx, dword ptr [rsp + 0x20]
003B9304  8B D1                           mov edx, ecx
003B9306  83 E1 07                        and ecx, 7
003B9309  48 C1 EA 03                     shr rdx, 3
003B930D  48 03 15 94 5E B4 00            add rdx, qword ptr [rip + 0xb45e94]
003B9314  0F BE 02                        movsx eax, byte ptr [rdx]
003B9317  0F B3 C8                        btr eax, ecx
003B931A  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
003B931E  88 02                           mov byte ptr [rdx], al
003B9320  8B D1                           mov edx, ecx
003B9322  48 C1 EA 03                     shr rdx, 3
003B9326  83 E1 07                        and ecx, 7
003B9329  48 03 15 78 5E B4 00            add rdx, qword ptr [rip + 0xb45e78]
003B9330  0F BE 02                        movsx eax, byte ptr [rdx]
003B9333  0F B3 C8                        btr eax, ecx
003B9336  8B 4C 24 28                     mov ecx, dword ptr [rsp + 0x28]
003B933A  88 02                           mov byte ptr [rdx], al
003B933C  8B D1                           mov edx, ecx
003B933E  48 C1 EA 03                     shr rdx, 3
003B9342  83 E1 07                        and ecx, 7
003B9345  48 03 15 5C 5E B4 00            add rdx, qword ptr [rip + 0xb45e5c]
003B934C  0F BE 02                        movsx eax, byte ptr [rdx]
003B934F  0F B3 C8                        btr eax, ecx
003B9352  88 02                           mov byte ptr [rdx], al
003B9354  48 83 C4 38                     add rsp, 0x38
003B9358  C3                              ret
003B9359  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTiClearBloomFilter(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m14;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m10 = 0;
    result = EtwpTiGetHashedBitNumbers(v_stack_m18, a2, a2, a4);
    a1 = (unsigned int)(((unsigned int)(v_stack_m18)) & (7));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m18)))) >> (3);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11820692));
    *(unsigned __int8 *)(a2) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a2)));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m14)))) >> (3);
    a1 = (unsigned int)(((unsigned int)(v_stack_m14)) & (7));
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11820664));
    *(unsigned __int8 *)(a2) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a2)));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m10)))) >> (3);
    a1 = (unsigned int)(((unsigned int)(v_stack_m10)) & (7));
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11820636));
    *(unsigned __int8 *)(a2) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a2)));
    v_rsp = (v_rsp) + (56);
    return (__int8)(*(unsigned __int8 *)(a2));
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTiClearBloomFilter(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m14;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m10 = 0;
    result = EtwpTiGetHashedBitNumbers(v_stack_m18, Arg2, Arg2, a4);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m18)) & (7));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m18)))) >> (3);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xB45E94));
    *(uint8_t *)(Arg2) = (uint8_t)((int8_t)(*(uint8_t *)(Arg2)));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m14)))) >> (3);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m14)) & (7));
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xB45E78));
    *(uint8_t *)(Arg2) = (uint8_t)((int8_t)(*(uint8_t *)(Arg2)));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m10)))) >> (3);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m10)) & (7));
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xB45E5C));
    *(uint8_t *)(Arg2) = (uint8_t)((int8_t)(*(uint8_t *)(Arg2)));
    local_rsp = (local_rsp) + (56);
    return (int8_t)(*(uint8_t *)(Arg2));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B92E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003B92E4[BB_003B92E4]
  bb_003B9359[BB_003B9359]
```
