# MiPreInitializeSystemImagePage

- RVA: `0x004D621C`–`0x004D62AC` (길이 `144` bytes)
- VA: `0x00000001404D621C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `36`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004D623A` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x004D6289` → [MiClearPfnReuseFields](../37/MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x004D6295` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x004D62A0` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [sub_00B42C66](../../page/B4/Unknown_function_00B42C66.md) at `0x00B42CEF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D621C  40 53                           push rbx
004D621E  48 83 EC 20                     sub rsp, 0x20
004D6222  48 8D 1C 49                     lea rbx, [rcx + rcx*2]
004D6226  48 C1 E3 04                     shl rbx, 4
004D622A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004D6234  48 03 D8                        add rbx, rax
004D6237  48 8B CB                        mov rcx, rbx
004D623A  E8 01 41 E4 FF                  call 0x14031a340
004D623F  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
004D6243  44 8A C8                        mov r9b, al
004D6246  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
004D6250  45 33 D2                        xor r10d, r10d
004D6253  48 23 C8                        and rcx, rax
004D6256  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
004D625A  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
004D625D  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004D6261  66 44 89 54 24 30               mov word ptr [rsp + 0x30], r10w
004D6267  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
004D626B  89 4B 20                        mov dword ptr [rbx + 0x20], ecx
004D626E  48 B9 00 00 00 00 00 FF FF FF   movabs rcx, 0xffffff0000000000
004D6278  4C 89 13                        mov qword ptr [rbx], r10
004D627B  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
004D627F  48 23 C1                        and rax, rcx
004D6282  48 8B CB                        mov rcx, rbx
004D6285  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
004D6289  E8 62 F7 E9 FF                  call 0x1403759f0
004D628E  48 8D 4B 10                     lea rcx, [rbx + 0x10]
004D6292  4C 89 11                        mov qword ptr [rcx], r10
004D6295  E8 02 47 DB FF                  call 0x14028a99c
004D629A  41 8A D1                        mov dl, r9b
004D629D  48 8B CB                        mov rcx, rbx
004D62A0  E8 3B 41 E4 FF                  call 0x14031a3e0
004D62A5  48 83 C4 20                     add rsp, 0x20
004D62A9  5B                              pop rbx
004D62AA  C3                              ret
004D62AB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPreInitializeSystemImagePage(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_rbx = (a1 + a1 * 2) << (4);
    v_rbx = (v_rbx) + (result);
    result = MiLockPageInline(v_rbx, a2, a3, a4);
    v_r10 = 0;
    a1 = (*(unsigned __int64 *)(v_rbx + 24)) & (result);
    *(unsigned __int64 *)(v_rbx + 24) = a1;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    v_stack_p8 = 0;
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    *(unsigned __int64 *)(v_rbx) = 0;
    result = (*(unsigned __int64 *)(v_rbx + 24)) & ((unsigned int)(v_stack_p8));
    *(unsigned __int64 *)(v_rbx + 24) = result;
    result = MiClearPfnReuseFields(v_rbx, a2, a3, (unsigned __int8)(result));
    *(unsigned __int64 *)(v_rbx + 16) = 0;
    result = MiSetOriginalPtePfnFromFreeList(v_rbx + 16, a2, a3, (unsigned __int8)(result));
    result = MiUnlockPage(v_rbx, (unsigned __int8)((unsigned __int8)(result)), a3, (unsigned __int8)(result));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiPreInitializeSystemImagePage(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    local_rbx = (Arg1 + Arg1 * 2) << (4);
    local_rbx = (local_rbx) + (result);
    result = MiLockPageInline(local_rbx, a2, a3, a4);
    local_r10 = 0;
    Arg1 = (*(uint64_t *)(local_rbx + 0x18)) & (result);
    *(void **)(local_rbx + 0x18) = Arg1;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    v_stack_p8 = 0;
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    *(uint64_t *)(local_rbx) = 0;
    result = (*(uint64_t *)(local_rbx + 0x18)) & ((uint32_t)(v_stack_p8));
    *(uint64_t *)(local_rbx + 0x18) = result;
    result = MiClearPfnReuseFields(local_rbx, a2, a3, (uint8_t)(result));
    *(uint64_t *)(local_rbx + 0x10) = 0;
    result = MiSetOriginalPtePfnFromFreeList(local_rbx + 16, a2, a3, (uint8_t)(result));
    result = MiUnlockPage(local_rbx, (uint8_t)((uint8_t)(result)), a3, (uint8_t)(result));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D621C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D621C[BB_004D621C]
  bb_004D62AB[BB_004D62AB]
```
