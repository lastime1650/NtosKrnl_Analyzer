# MiCheckLockUnlockByVa

- RVA: `0x00673D7C`–`0x00673DDD` (길이 `97` bytes)
- VA: `0x0000000140673D7C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000805BC`
- 디코드: `27`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00673D9F` → [MiTransformVadSecure](../../page/A2/MiTransformVadSecure_function_00A21278.md) (function, `0x00A21278`)
- `0x00673DAC` → [MiObtainReferencedSecureVad](../29/MiObtainReferencedSecureVad_function_00295688.md) (function, `0x00295688`)
- `0x00673DCF` → [MiUnlockAndDereferenceVad](../31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)

### Direct callers
- [MmLockPhysicalPagesByVa](../../page/7F/MmLockPhysicalPagesByVa_function_007FB930.md) at `0x007FB99A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00673D9F` → [MiTransformVadSecure](../../page/A2/MiTransformVadSecure_function_00A21278.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00673D7C  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00673D81  53                              push rbx
00673D82  48 83 EC 20                     sub rsp, 0x20
00673D86  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00673D8F  33 DB                           xor ebx, ebx
00673D91  49 8B D0                        mov rdx, r8
00673D94  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00673D98  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00673D9F  E8 D4 D4 3A 00                  call 0x140a21278
00673DA4  48 8B C8                        mov rcx, rax
00673DA7  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00673DAC  E8 D7 18 C2 FF                  call 0x140295688
00673DB1  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00673DB4  83 E1 70                        and ecx, 0x70
00673DB7  83 F9 10                        cmp ecx, 0x10
00673DBA  74 10                           je 0x140673dcc
00673DBC  83 C1 D0                        add ecx, -0x30
00673DBF  F7 C1 EF FF FF FF               test ecx, 0xffffffef
00673DC5  74 05                           je 0x140673dcc
00673DC7  BB 01 00 00 00                  mov ebx, 1
00673DCC  48 8B C8                        mov rcx, rax
00673DCF  E8 8C 30 CA FF                  call 0x140316e60
00673DD4  8B C3                           mov eax, ebx
00673DD6  48 83 C4 20                     add rsp, 0x20
00673DDA  5B                              pop rbx
00673DDB  C3                              ret
00673DDC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCheckLockUnlockByVa(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    v_stack_p10 = 0;
    result = MiTransformVadSecure(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a3, a4);
    result = MiObtainReferencedSecureVad(result, v_stack_p10, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (112));
    if (((unsigned int)(a1)) == 16) goto loc_00673DCC;
    a1 = (unsigned int)((a1) + (-48));
    if ((((unsigned int)(a1)) & (0xFFFFFFEFULL)) != 0) {
        v_rbx = 1;
    }
    result = MiUnlockAndDereferenceVad(result, v_stack_p10, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t MiCheckLockUnlockByVa(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    v_stack_p10 = 0;
    result = MiTransformVadSecure(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg3, a4);
    result = MiObtainReferencedSecureVad(result, v_stack_p10, Arg3, a4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (112));
    if (((uint32_t)(Arg1)) == 16) goto loc_00673DCC;
    Arg1 = (uint32_t)((Arg1) + (-48));
    if ((((uint32_t)(Arg1)) & (0xFFFFFFEFULL)) != 0) {
        local_rbx = 1;
    }
    result = MiUnlockAndDereferenceVad(result, v_stack_p10, Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00673D7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00673D7C[BB_00673D7C]
  bb_00673DBC[BB_00673DBC]
  bb_00673DC7[BB_00673DC7]
  bb_00673DCC[BB_00673DCC]
  bb_00673DDC[BB_00673DDC]
  bb_00673D7C -->|branch| bb_00673DCC
  bb_00673D7C -->|fallthrough| bb_00673DBC
  bb_00673DBC -->|branch| bb_00673DCC
  bb_00673DBC -->|fallthrough| bb_00673DC7
  bb_00673DC7 -->|flow| bb_00673DCC
```
