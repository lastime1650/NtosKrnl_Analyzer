# MiUnlockPagedAddress

- RVA: `0x00492FC4`–`0x0049303B` (길이 `119` bytes)
- VA: `0x0000000140492FC4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `28`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00493016` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00493020` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x0049302A` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiFreeClonePool](MiFreeClonePool_function_00492EE0.md) at `0x00492F1A`
- [MiFreeCombinePool](MiFreeCombinePool_function_00492F60.md) at `0x00492F95`
- [MiLockPagedRange](../../page/A6/MiLockPagedRange_function_00A6C8C0.md) at `0x00A6C91C`
- [MiFreeCloneDescriptor](../../page/A8/MiFreeCloneDescriptor_function_00A89F0C.md) at `0x00A89F41`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00492FC4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00492FC9  57                              push rdi
00492FCA  48 83 EC 20                     sub rsp, 0x20
00492FCE  48 C1 E9 09                     shr rcx, 9
00492FD2  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00492FDC  48 23 C8                        and rcx, rax
00492FDF  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00492FE9  48 8B 04 01                     mov rax, qword ptr [rcx + rax]
00492FED  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00492FF7  48 C1 E8 0C                     shr rax, 0xc
00492FFB  48 23 C1                        and rax, rcx
00492FFE  48 8D 3C 40                     lea rdi, [rax + rax*2]
00493002  48 C1 E7 04                     shl rdi, 4
00493006  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00493010  48 03 F8                        add rdi, rax
00493013  48 8B CF                        mov rcx, rdi
00493016  E8 25 73 E8 FF                  call 0x14031a340
0049301B  48 8B CF                        mov rcx, rdi
0049301E  8A D8                           mov bl, al
00493020  E8 AB 29 DB FF                  call 0x1402459d0
00493025  8A D3                           mov dl, bl
00493027  48 8B CF                        mov rcx, rdi
0049302A  E8 B1 73 E8 FF                  call 0x14031a3e0
0049302F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00493034  48 83 C4 20                     add rsp, 0x20
00493038  5F                              pop rdi
00493039  C3                              ret
0049303A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockPagedAddress(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) >> (9);
    a1 = (a1) & (result);
    result = (*(unsigned __int64 *)(a1 + result * 1)) >> (12);
    result = (result) & (a1);
    v_rdi = (result + result * 2) << (4);
    v_rdi = (v_rdi) + (result);
    result = MiLockPageInline(v_rdi, a2, a3, a4);
    result = MiRemoveLockedPageChargeAndDecRef(v_rdi, a2, a3, a4);
    result = MiUnlockPage(v_rdi, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockPagedAddress(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (result);
    result = (*(uint64_t *)(Arg1 + result * 1)) >> (12);
    result = (result) & (Arg1);
    local_rdi = (result + result * 2) << (4);
    local_rdi = (local_rdi) + (result);
    result = MiLockPageInline(local_rdi, a2, a3, a4);
    result = MiRemoveLockedPageChargeAndDecRef(local_rdi, a2, a3, a4);
    result = MiUnlockPage(local_rdi, (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00492FC4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00492FC4[BB_00492FC4]
  bb_0049303A[BB_0049303A]
```
