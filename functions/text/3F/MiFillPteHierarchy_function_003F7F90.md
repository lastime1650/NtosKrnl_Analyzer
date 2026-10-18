# MiFillPteHierarchy

- RVA: `0x003F7F90`–`0x003F7FE9` (길이 `89` bytes)
- VA: `0x00000001403F7F90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `24`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiSynchronizeSystemVa](../28/MiSynchronizeSystemVa_function_0028ECB8.md) at `0x0028EE98`
- [MiFindActualFaultingPte](../32/MiFindActualFaultingPte_function_0032899C.md) at `0x00328B4F`
- [MmFreeContiguousMemory](MmFreeContiguousMemory_function_003F6F60.md) at `0x003F6FAD`
- [MiCreateSystemPageTable](../45/MiCreateSystemPageTable_function_004518D0.md) at `0x00451AC3`
- [MiKcsanPopulateHierarchy](../67/MiKcsanPopulateHierarchy_function_0067FB0C.md) at `0x0067FB3B`
- [MiKcsanPopulateHierarchy](../67/MiKcsanPopulateHierarchy_function_0067FB0C.md) at `0x0067FB48`
- [MiDbgCopyMemoryTarget](../68/MiDbgCopyMemoryTarget_function_00684E70.md) at `0x00684EE3`
- [MiMapProcessExecutable](../../page/8C/MiMapProcessExecutable_function_008CFDB4.md) at `0x008CFEE5`
- [MiUpdateForkMaps](../../page/A7/MiUpdateForkMaps_function_00A7DAF8.md) at `0x00A7DBAA`
- [MxMapVa](../../init/C6/MxMapVa_function_00C63EC4.md) at `0x00C63EF2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F7F90  48 C1 E9 09                     shr rcx, 9
003F7F94  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
003F7F9E  49 23 C9                        and rcx, r9
003F7FA1  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
003F7FAB  49 8B C0                        mov rax, r8
003F7FAE  48 03 C8                        add rcx, rax
003F7FB1  48 89 0A                        mov qword ptr [rdx], rcx
003F7FB4  48 C1 E9 09                     shr rcx, 9
003F7FB8  49 23 C9                        and rcx, r9
003F7FBB  49 8B C0                        mov rax, r8
003F7FBE  48 03 C8                        add rcx, rax
003F7FC1  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003F7FC5  48 C1 E9 09                     shr rcx, 9
003F7FC9  49 23 C9                        and rcx, r9
003F7FCC  49 8B C0                        mov rax, r8
003F7FCF  48 03 C8                        add rcx, rax
003F7FD2  48 89 4A 10                     mov qword ptr [rdx + 0x10], rcx
003F7FD6  48 C1 E9 09                     shr rcx, 9
003F7FDA  49 23 C9                        and rcx, r9
003F7FDD  49 8B C0                        mov rax, r8
003F7FE0  48 03 C8                        add rcx, rax
003F7FE3  48 89 4A 18                     mov qword ptr [rdx + 0x18], rcx
003F7FE7  C3                              ret
003F7FE8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFillPteHierarchy(__int64 a1, __int64 a2)
{
    a1 = (a1) >> (9);
    a1 = (a1) & (a4);
    a1 = (a1) + (a3);
    *(unsigned __int64 *)(a2) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a4);
    a1 = (a1) + (a3);
    *(unsigned __int64 *)(a2 + 8) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a4);
    a1 = (a1) + (a3);
    *(unsigned __int64 *)(a2 + 16) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a4);
    a1 = (a1) + (a3);
    *(unsigned __int64 *)(a2 + 24) = a1;
    return a3;
}
```

## 5. (Beta) C Style

```c
int64_t MiFillPteHierarchy(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (a4);
    Arg1 = (Arg1) + (a3);
    *(uint64_t *)(arg2) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (a4);
    Arg1 = (Arg1) + (a3);
    *(uint64_t *)(arg2 + 0x8) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (a4);
    Arg1 = (Arg1) + (a3);
    *(uint64_t *)(arg2 + 0x10) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (a4);
    Arg1 = (Arg1) + (a3);
    *(uint64_t *)(arg2 + 0x18) = Arg1;
    return a3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F7F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F7F90[BB_003F7F90]
  bb_003F7FE8[BB_003F7FE8]
```
