# MiReadyLargeAwePageForFree

- RVA: `0x00689258`–`0x006892B8` (길이 `96` bytes)
- VA: `0x0000000140689258`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `26`개 명령, `96/96` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00689265` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x0068926F` → [MiClearAweLargePageMetadata](MiClearAweLargePageMetadata_function_006880EC.md) (function, `0x006880EC`)
- `0x006892A7` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiFreePhysicalPageChain](../2A/MiFreePhysicalPageChain_function_002A9F1C.md) at `0x002AA044`
- [MiFreeAwePagesFromMdl](MiFreeAwePagesFromMdl_function_00688984.md) at `0x006889E5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00689258  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0068925D  57                              push rdi
0068925E  48 83 EC 20                     sub rsp, 0x20
00689262  48 8B F9                        mov rdi, rcx
00689265  E8 D6 10 C9 FF                  call 0x14031a340
0068926A  48 8B CF                        mov rcx, rdi
0068926D  8A D8                           mov bl, al
0068926F  E8 78 EE FF FF                  call 0x1406880ec
00689274  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
00689278  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
00689282  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
00689286  48 8B CF                        mov rcx, rdi
00689289  4C 8D 42 01                     lea r8, [rdx + 1]
0068928D  4D 8B C8                        mov r9, r8
00689290  4C 33 CA                        xor r9, rdx
00689293  8A D3                           mov dl, bl
00689295  4C 23 C8                        and r9, rax
00689298  4D 33 C8                        xor r9, r8
0068929B  4C 89 4F 18                     mov qword ptr [rdi + 0x18], r9
0068929F  48 C7 47 10 00 00 00 00         mov qword ptr [rdi + 0x10], 0
006892A7  E8 34 11 C9 FF                  call 0x14031a3e0
006892AC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
006892B1  48 83 C4 20                     add rsp, 0x20
006892B5  5F                              pop rdi
006892B6  C3                              ret
006892B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReadyLargeAwePageForFree(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MiLockPageInline(a1, a2, a3, a4);
    result = MiClearAweLargePageMetadata(a1, a2, a3, a4);
    a4 = (*(unsigned __int64 *)(a1 + 24) + 1) ^ (*(unsigned __int64 *)(a1 + 24));
    a4 = (a4) & (result);
    a4 = (a4) ^ (*(unsigned __int64 *)(a1 + 24) + 1);
    *(unsigned __int64 *)(a1 + 24) = a4;
    *(unsigned __int64 *)(a1 + 16) = 0;
    result = MiUnlockPage(a1, (unsigned __int8)((unsigned __int8)(result)), *(unsigned __int64 *)(a1 + 24) + 1, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReadyLargeAwePageForFree(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MiLockPageInline(Arg1, a2, a3, a4);
    result = MiClearAweLargePageMetadata(Arg1, a2, a3, a4);
    a4 = (*(uint64_t *)(arg1 + 0x18) + 1) ^ (*(uint64_t *)(arg1 + 0x18));
    a4 = (a4) & (result);
    a4 = (a4) ^ (*(uint64_t *)(arg1 + 0x18) + 1);
    *(uint64_t *)(arg1 + 0x18) = a4;
    *(uint64_t *)(arg1 + 0x10) = 0;
    result = MiUnlockPage(Arg1, (uint8_t)((uint8_t)(result)), *(uint64_t *)(arg1 + 0x18) + 1, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00689258&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00689258[BB_00689258]
  bb_006892B7[BB_006892B7]
```
