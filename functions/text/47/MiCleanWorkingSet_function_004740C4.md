# MiCleanWorkingSet

- RVA: `0x004740C4`–`0x0047413C` (길이 `120` bytes)
- VA: `0x00000001404740C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FD94`
- 디코드: `31`개 명령, `120/120` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004740E0` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x00474113` → [MiDrainSystemAccessLog](MiDrainSystemAccessLog_function_00474144.md) (function, `0x00474144`)
- `0x00474122` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)

### Direct callers
- [MmCleanProcessAddressSpace](../../page/A1/MmCleanProcessAddressSpace_function_00A17EC0.md) at `0x00A18090`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004740C4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004740C9  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
004740CE  57                              push rdi
004740CF  48 83 EC 20                     sub rsp, 0x20
004740D3  48 8D B1 00 04 00 00            lea rsi, [rcx + 0x400]
004740DA  48 8B D9                        mov rbx, rcx
004740DD  48 8B CE                        mov rcx, rsi
004740E0  E8 BB F7 EA FF                  call 0x1403238a0
004740E5  8B 96 B8 00 00 00               mov edx, dword ptr [rsi + 0xb8]
004740EB  48 8B CE                        mov rcx, rsi
004740EE  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
004740F2  40 8A F8                        mov dil, al
004740F5  C1 EA 18                        shr edx, 0x18
004740F8  80 CA 01                        or dl, 1
004740FB  88 54 24 33                     mov byte ptr [rsp + 0x33], dl
004740FF  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00474103  C1 EA 18                        shr edx, 0x18
00474106  88 96 BB 00 00 00               mov byte ptr [rsi + 0xbb], dl
0047410C  48 FF 8B 88 02 00 00            dec qword ptr [rbx + 0x288]
00474113  E8 2C 00 00 00                  call 0x140474144
00474118  48 8B 5E 70                     mov rbx, qword ptr [rsi + 0x70]
0047411C  40 8A D7                        mov dl, dil
0047411F  48 8B CE                        mov rcx, rsi
00474122  E8 49 AB E0 FF                  call 0x14027ec70
00474127  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0047412C  48 8D 43 FC                     lea rax, [rbx - 4]
00474130  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00474135  48 83 C4 20                     add rsp, 0x20
00474139  5F                              pop rdi
0047413A  C3                              ret
0047413B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCleanWorkingSet(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pB;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = MiLockWorkingSetExclusive(a1 + 1024, a2, a3, a4);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1024 + 184)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1024 + 184))) >> (24));
    a2 = (unsigned __int8)((a2) | (1));
    v_stack_pB = (unsigned __int8)(a2);
    a2 = (unsigned int)(((unsigned int)(v_stack_p8)) >> (24));
    *(unsigned __int8 *)(a1 + 1024 + 187) = (unsigned __int8)(a2);
    result = MiDrainSystemAccessLog(a1 + 1024, a2, a3, a4);
    result = MiUnlockWorkingSetExclusive(a1 + 1024, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 1024 + 112) - 4;
}
```

## 5. (Beta) C Style

```c
int64_t MiCleanWorkingSet(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;
    uint8_t v_stack_pB;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = MiLockWorkingSetExclusive(Arg1 + 1024, a2, a3, a4);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x400 + 0xB8)));
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x400 + 0xB8))) >> (24));
    a2 = (uint8_t)((a2) | (1));
    v_stack_pB = (uint8_t)(a2);
    a2 = (uint32_t)(((uint32_t)(v_stack_p8)) >> (24));
    *(uint8_t *)(arg1 + 0x400 + 0xBB) = (uint8_t)(a2);
    result = MiDrainSystemAccessLog(Arg1 + 1024, a2, a3, a4);
    result = MiUnlockWorkingSetExclusive(Arg1 + 1024, (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0x400 + 0x70) - 4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xBB` | `8` | `W` |
| `Arg1` | `+ 0x288` | `64` | `R/W` |
| `Arg1` | `+ 0x400` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004740C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004740C4[BB_004740C4]
  bb_0047413B[BB_0047413B]
```
