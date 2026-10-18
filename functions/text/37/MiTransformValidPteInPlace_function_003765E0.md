# MiTransformValidPteInPlace

- RVA: `0x003765E0`–`0x0037663A` (길이 `90` bytes)
- VA: `0x00000001403765E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007AC30`
- 디코드: `27`개 명령, `90/90` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00376608` → [MiTransformValidPteUsingAccessedBit](MiTransformValidPteUsingAccessedBit_function_00376640.md) (function, `0x00376640`)
- `0x00376633` → [MiTransformValidPteViaIpi](../68/MiTransformValidPteViaIpi_function_0068A978.md) (function, `0x0068A978`)

### Direct callers
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B360A`
- [MiTradeActivePage](MiTradeActivePage_function_00374424.md) at `0x003746D4`
- [MiInitializeSystemPageTable](../45/MiInitializeSystemPageTable_function_00451C88.md) at `0x00451F50`
- [MiShadowTopLevelPxes](../46/MiShadowTopLevelPxes_function_0046C6B0.md) at `0x0046C7DC`
- [MiMakeLargePageTable](../4F/MiMakeLargePageTable_function_004F9198.md) at `0x004F938E`
- [MiPfnRangeIsZero](../67/MiPfnRangeIsZero_function_006735C0.md) at `0x00673840`
- [MiInitializeDynamicBitmap](../67/MiInitializeDynamicBitmap_function_0067F5BC.md) at `0x0067F7B4`
- [MiDemoteValidLargePageOneLevel](../68/MiDemoteValidLargePageOneLevel_function_0068A3F4.md) at `0x0068A7CA`
- [MiReplicatePteChangeToProcess](../69/MiReplicatePteChangeToProcess_function_00693D24.md) at `0x00693DA1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003765E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003765E5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
003765EA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003765EF  57                              push rdi
003765F0  48 83 EC 30                     sub rsp, 0x30
003765F4  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
003765F8  41 8B F9                        mov edi, r9d
003765FB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003765FF  49 8B D8                        mov rbx, r8
00376602  48 8B F2                        mov rsi, rdx
00376605  48 8B E9                        mov rbp, rcx
00376608  E8 33 00 00 00                  call 0x140376640
0037660D  85 C0                           test eax, eax
0037660F  74 16                           je 0x140376627
00376611  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00376616  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0037661B  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00376620  48 83 C4 30                     add rsp, 0x30
00376624  5F                              pop rdi
00376625  C3                              ret
00376626  CC                              int3
00376627  44 8B CF                        mov r9d, edi
0037662A  4C 8B C3                        mov r8, rbx
0037662D  48 8B D6                        mov rdx, rsi
00376630  48 8B CD                        mov rcx, rbp
00376633  E8 40 43 31 00                  call 0x14068a978
00376638  EB D7                           jmp 0x140376611
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiTransformValidPteInPlace(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = (unsigned int)((unsigned int)(a5));
    result = MiTransformValidPteUsingAccessedBit(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00376627;
loc_00376611:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00376627:
    result = MiTransformValidPteViaIpi(v_stack_p10, v_stack_p18, v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a4))));
    goto loc_00376611;
}
```

## 5. (Beta) C Style

```c
int64_t MiTransformValidPteInPlace(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg5));
    result = MiTransformValidPteUsingAccessedBit(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00376627;
loc_00376611:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00376627:
    result = MiTransformValidPteViaIpi(v_stack_p10, v_stack_p18, v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    goto loc_00376611;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003765E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003765E0[BB_003765E0]
  bb_00376611[BB_00376611]
  bb_00376626[BB_00376626]
  bb_00376627[BB_00376627]
  bb_003765E0 -->|branch| bb_00376627
  bb_003765E0 -->|fallthrough| bb_00376611
  bb_00376626 -->|flow| bb_00376627
  bb_00376627 -->|branch| bb_00376611
```
