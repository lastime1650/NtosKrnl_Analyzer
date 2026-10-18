# RtlpRemoveInvertedFunctionTableEntry

- RVA: `0x005EF354`–`0x005EF3B6` (길이 `98` bytes)
- VA: `0x00000001405EF354`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `25`개 명령, `98/98` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005EF39E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [sub_006EE978](../6E/Unknown_function_006EE978.md) at `0x006EE98F`

### Static image references
- `0x005EF35B` → RVA `0x01200028` (`CFGRO`; read/write)
- `0x005EF362` → RVA `0x01200020` (`CFGRO`; read)
- `0x005EF3A3` → RVA `0x01200020` (`CFGRO`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EF354  48 83 EC 28                     sub rsp, 0x28
005EF358  44 8B CA                        mov r9d, edx
005EF35B  F0 FF 05 C6 0C C1 00            lock inc dword ptr [rip + 0xc10cc6]
005EF362  8B 05 B8 0C C1 00               mov eax, dword ptr [rip + 0xc10cb8]
005EF368  83 F8 02                        cmp eax, 2
005EF36B  74 36                           je 0x1405ef3a3
005EF36D  41 2B C1                        sub eax, r9d
005EF370  4C 8D 15 A9 0C C1 00            lea r10, [rip + 0xc10ca9]
005EF377  FF C8                           dec eax
005EF379  4C 8D 04 40                     lea r8, [rax + rax*2]
005EF37D  41 8D 41 01                     lea eax, [r9 + 1]
005EF381  49 C1 E0 03                     shl r8, 3
005EF385  8B C8                           mov ecx, eax
005EF387  48 FF C0                        inc rax
005EF38A  48 8D 04 41                     lea rax, [rcx + rax*2]
005EF38E  49 8D 49 01                     lea rcx, [r9 + 1]
005EF392  49 8D 0C 49                     lea rcx, [r9 + rcx*2]
005EF396  49 8D 0C CA                     lea rcx, [r10 + rcx*8]
005EF39A  49 8D 14 C2                     lea rdx, [r10 + rax*8]
005EF39E  E8 9D 74 0D 00                  call 0x1406c6840
005EF3A3  FF 0D 77 0C C1 00               dec dword ptr [rip + 0xc10c77]
005EF3A9  F0 FF 05 78 0C C1 00            lock inc dword ptr [rip + 0xc10c78]
005EF3B0  48 83 C4 28                     add rsp, 0x28
005EF3B4  C3                              ret
005EF3B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpRemoveInvertedFunctionTableEntry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(v_rip + 12651704));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12651704)))) != 2) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12651704))) - ((unsigned int)((unsigned int)(a2))));
        v_r10 = v_rip + 12651689;
        result = (unsigned int)((result) - 1);
        a3 = result + result * 2;
        result = (unsigned int)(a2) + 1;
        a3 = (a3) << (3);
        a1 = (unsigned int)(result);
        result = (result) + 1;
        result = a1 + result * 2;
        a1 = (unsigned int)(a2) + 1;
        a1 = (unsigned int)(a2) + a1 * 2;
        a1 = v_r10 + a1 * 8;
        a2 = v_r10 + result * 8;
        result = memcpy(a1, a2, a3, (unsigned int)(a2));
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpRemoveInvertedFunctionTableEntry(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC10CB8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC10CB8)))) != 2) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC10CB8))) - ((uint32_t)((uint32_t)(Arg2))));
        local_r10 = v_rip + 12651689;
        result = (uint32_t)((result) - 1);
        a3 = result + result * 2;
        result = (uint32_t)(Arg2) + 1;
        a3 = (a3) << (3);
        Arg1 = (uint32_t)(result);
        result = (result) + 1;
        result = Arg1 + result * 2;
        Arg1 = (uint32_t)(Arg2) + 1;
        Arg1 = (uint32_t)(Arg2) + Arg1 * 2;
        Arg1 = local_r10 + Arg1 * 8;
        Arg2 = local_r10 + result * 8;
        result = memcpy(Arg1, Arg2, a3, (uint32_t)(Arg2));
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg2` | `+ 0x0 + rcx*2` | `64` | `R` |
| `Arg2` | `+ 0x1` | `32` | `R` |
| `Arg2` | `+ 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EF354&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EF354[BB_005EF354]
  bb_005EF36D[BB_005EF36D]
  bb_005EF3A3[BB_005EF3A3]
  bb_005EF3B5[BB_005EF3B5]
  bb_005EF354 -->|branch| bb_005EF3A3
  bb_005EF354 -->|fallthrough| bb_005EF36D
  bb_005EF36D -->|flow| bb_005EF3A3
```
