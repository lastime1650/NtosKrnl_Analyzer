# MiPrefetchReleasePreallocatedPages

- RVA: `0x004BE374`–`0x004BE3CA` (길이 `86` bytes)
- VA: `0x00000001404BE374`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `25`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BE399` → [MiFreePageChain](../37/MiFreePageChain_function_00377D9C.md) (function, `0x00377D9C`)
- `0x004BE3B0` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)

### Direct callers
- [MiPrefetchPreallocatePages](../36/MiPrefetchPreallocatePages_function_0036B1F0.md) at `0x0036B39D`
- [MiPrefetchPreallocatePages](../36/MiPrefetchPreallocatePages_function_0036B1F0.md) at `0x0036B4AD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BE374  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004BE379  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
004BE37E  57                              push rdi
004BE37F  48 83 EC 20                     sub rsp, 0x20
004BE383  48 83 21 00                     and qword ptr [rcx], 0
004BE387  48 8B F9                        mov rdi, rcx
004BE38A  48 83 61 08 00                  and qword ptr [rcx + 8], 0
004BE38F  41 8B D9                        mov ebx, r9d
004BE392  48 8D 4A 58                     lea rcx, [rdx + 0x58]
004BE396  49 8B F0                        mov rsi, r8
004BE399  E8 FE 99 EB FF                  call 0x140377d9c
004BE39E  85 DB                           test ebx, ebx
004BE3A0  74 17                           je 0x1404be3b9
004BE3A2  83 7F 10 00                     cmp dword ptr [rdi + 0x10], 0
004BE3A6  74 11                           je 0x1404be3b9
004BE3A8  BA 00 02 00 00                  mov edx, 0x200
004BE3AD  48 8B CE                        mov rcx, rsi
004BE3B0  E8 E7 45 E6 FF                  call 0x14032299c
004BE3B5  83 67 10 00                     and dword ptr [rdi + 0x10], 0
004BE3B9  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004BE3BE  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004BE3C3  48 83 C4 20                     add rsp, 0x20
004BE3C7  5F                              pop rdi
004BE3C8  C3                              ret
004BE3C9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPrefetchReleasePreallocatedPages(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = MiFreePageChain(a2 + 88, a2, a3, a4);
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_004BE3B9;
    if ((*(unsigned int *)(a1 + 16)) != 0) {
        a2 = 512;
        a1 = a3;
        result = MiReleaseNonPagedResources(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiPrefetchReleasePreallocatedPages(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = MiFreePageChain(Arg2 + 88, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_004BE3B9;
    if ((*(uint32_t *)(arg1 + 0x10)) != 0) {
        Arg2 = 512;
        Arg1 = Arg3;
        result = MiReleaseNonPagedResources(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R/W` |
| `Arg2` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BE374&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BE374[BB_004BE374]
  bb_004BE3A2[BB_004BE3A2]
  bb_004BE3A8[BB_004BE3A8]
  bb_004BE3B9[BB_004BE3B9]
  bb_004BE3C9[BB_004BE3C9]
  bb_004BE374 -->|branch| bb_004BE3B9
  bb_004BE374 -->|fallthrough| bb_004BE3A2
  bb_004BE3A2 -->|branch| bb_004BE3B9
  bb_004BE3A2 -->|fallthrough| bb_004BE3A8
  bb_004BE3A8 -->|flow| bb_004BE3B9
```
