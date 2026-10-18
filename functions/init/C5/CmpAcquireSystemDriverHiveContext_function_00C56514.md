# CmpAcquireSystemDriverHiveContext

- RVA: `0x00C56514`–`0x00C5657B` (길이 `103` bytes)
- VA: `0x0000000140C56514`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `30`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C5652C` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x00C5655A` → [CmpFindControlSet](../../page/7F/CmpFindControlSet_function_007F1A34.md) (function, `0x007F1A34`)

### Direct callers
- [CmGetSystemDriverList](../C7/CmGetSystemDriverList_function_00C7380C.md) at `0x00C73AC7`
- [CmGetSystemDriverList](../C7/CmGetSystemDriverList_function_00C7380C.md) at `0x00C73ADE`
- [CmGetSystemDriverList](../C7/CmGetSystemDriverList_function_00C7380C.md) at `0x00C73AFD`

### Static image references
- `0x00C56540` → RVA `0x00B4AFC8` (`CmpCurrentString`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C5652C` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`INIT` → `PAGECMRC`)
  - `0x00C5655A` → [CmpFindControlSet](../../page/7F/CmpFindControlSet_function_007F1A34.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C56514  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C56519  57                              push rdi
00C5651A  48 83 EC 20                     sub rsp, 0x20
00C5651E  48 8B F9                        mov rdi, rcx
00C56521  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
00C56526  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00C5652A  33 D2                           xor edx, edx
00C5652C  E8 9F 32 F7 FF                  call 0x140bc97d0
00C56531  8B D8                           mov ebx, eax
00C56533  85 C0                           test eax, eax
00C56535  78 36                           js 0x140c5656d
00C56537  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
00C5653B  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00C56540  4C 8D 05 81 4A EF FF            lea r8, [rip - 0x10b57f]
00C56547  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
00C5654B  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00C5654F  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
00C56553  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00C56557  8B 52 28                        mov edx, dword ptr [rdx + 0x28]
00C5655A  E8 D5 B4 B9 FF                  call 0x1407f1a34
00C5655F  83 F8 FF                        cmp eax, -1
00C56562  89 47 38                        mov dword ptr [rdi + 0x38], eax
00C56565  B9 25 02 00 C0                  mov ecx, 0xc0000225
00C5656A  0F 44 D9                        cmove ebx, ecx
00C5656D  8B C3                           mov eax, ebx
00C5656F  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00C56574  48 83 C4 20                     add rsp, 0x20
00C56578  5F                              pop rdi
00C56579  C3                              ret
00C5657A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpAcquireSystemDriverHiveContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_stack_p8 = 0;
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = *(unsigned __int64 *)(a1 + 40);
        a4 = v_stack_p8;
        a3 = v_rip - 1095039;
        a1 = *(unsigned __int64 *)(a2 + 8);
        a1 = *(unsigned __int64 *)(a1 + 32);
        *(unsigned __int64 *)(a1 + 48) = a1;
        a2 = *(unsigned __int64 *)(a2 + 8);
        a2 = *(unsigned int *)(a2 + 40);
        result = CmpFindControlSet(a1, a2, a3, a4);
        *(unsigned int *)(a1 + 56) = (unsigned int)(result);
        a1 = 0xC0000225ULL;
        v_rbx = (unsigned int)((unsigned int)(result));
        if (((unsigned int)(result)) == -1) { v_rbx = (unsigned int)(a1); }
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t CmpAcquireSystemDriverHiveContext(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    v_stack_p8 = 0;
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(*(uint64_t *)(arg1 + 0x28), Arg2, a3, a4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = *(uint64_t *)(arg1 + 0x28);
        a4 = v_stack_p8;
        a3 = v_rip - 1095039;
        Arg1 = *(uint64_t *)(Arg2 + 0x8);
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        *(void **)(arg1 + 0x30) = Arg1;
        Arg2 = *(uint64_t *)(Arg2 + 0x8);
        Arg2 = *(uint32_t *)(Arg2 + 0x28);
        result = CmpFindControlSet(Arg1, Arg2, a3, a4);
        *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
        Arg1 = 0xC0000225ULL;
        local_rbx = (uint32_t)((uint32_t)(result));
        if (((uint32_t)(result)) == -1) { local_rbx = (uint32_t)(Arg1); }
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C56514&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C56514[BB_00C56514]
  bb_00C56537[BB_00C56537]
  bb_00C5656D[BB_00C5656D]
  bb_00C5657A[BB_00C5657A]
  bb_00C56514 -->|branch| bb_00C5656D
  bb_00C56514 -->|fallthrough| bb_00C56537
  bb_00C56537 -->|flow| bb_00C5656D
```
