# ST_STORE&lt;SM_TRAITS&gt;::StDmpDummyPageRecordAllocate

- RVA: `0x004BC160`–`0x004BC1D4` (길이 `116` bytes)
- VA: `0x00000001404BC160`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BD2C`
- 디코드: `31`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BC170` → [SmHpChunkAlloc](../26/SmHpChunkAlloc_function_002688E0.md) (function, `0x002688E0`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmpSinglePageAdd](../20/ST_STORE_SM_TRAITS_StDmpSinglePageAdd_function_0020502C.md) at `0x00205254`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BC160  40 53                           push rbx
004BC162  48 83 EC 20                     sub rsp, 0x20
004BC166  48 8B D9                        mov rbx, rcx
004BC169  48 81 C1 C0 00 00 00            add rcx, 0xc0
004BC170  E8 6B C7 DA FF                  call 0x1402688e0
004BC175  45 33 C9                        xor r9d, r9d
004BC178  48 89 83 F8 02 00 00            mov qword ptr [rbx + 0x2f8], rax
004BC17F  48 85 C0                        test rax, rax
004BC182  74 48                           je 0x1404bc1cc
004BC184  33 C9                           xor ecx, ecx
004BC186  33 D2                           xor edx, edx
004BC188  48 89 08                        mov qword ptr [rax], rcx
004BC18B  89 48 08                        mov dword ptr [rax + 8], ecx
004BC18E  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
004BC195  8B 8B C8 01 00 00               mov ecx, dword ptr [rbx + 0x1c8]
004BC19B  4C 8B C0                        mov r8, rax
004BC19E  2B 83 D8 01 00 00               sub eax, dword ptr [rbx + 0x1d8]
004BC1A4  49 81 E0 00 F0 FF FF            and r8, 0xfffffffffffff000
004BC1AB  41 2B C0                        sub eax, r8d
004BC1AE  F7 B3 D0 01 00 00               div dword ptr [rbx + 0x1d0]
004BC1B4  41 8B 50 10                     mov edx, dword ptr [r8 + 0x10]
004BC1B8  D3 E2                           shl edx, cl
004BC1BA  03 C2                           add eax, edx
004BC1BC  89 83 00 03 00 00               mov dword ptr [rbx + 0x300], eax
004BC1C2  41 8B C1                        mov eax, r9d
004BC1C5  48 83 C4 20                     add rsp, 0x20
004BC1C9  5B                              pop rbx
004BC1CA  C3                              ret
004BC1CB  CC                              int3
004BC1CC  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
004BC1D2  EB EE                           jmp 0x1404bc1c2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StDmpDummyPageRecordAllocate(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (192);
    result = SmHpChunkAlloc(a1, a2, a3, a4);
    a4 = 0;
    *(unsigned __int64 *)(a1 + 760) = result;
    if (result == 0) goto loc_004BC1CC;
    a1 = 0;
    a2 = 0;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned int *)(result + 8) = 0;
    result = (unsigned int)((*(unsigned __int64 *)(a1 + 760)) - (*(unsigned int *)(a1 + 472)));
    a3 = (*(unsigned __int64 *)(a1 + 760)) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((result) - ((unsigned int)(a3)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 16))) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 456)))));
    result = (unsigned int)((result) + (a2));
    *(unsigned int *)(a1 + 768) = (unsigned int)(result);
loc_004BC1C2:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_004BC1CC:
    goto loc_004BC1C2;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StDmpDummyPageRecordAllocate(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (192);
    result = SmHpChunkAlloc(Arg1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    *(uint64_t *)(arg1 + 0x2F8) = result;
    if (result == 0) goto loc_004BC1CC;
    Arg1 = 0;
    Arg2 = 0;
    *(uint64_t *)(result) = 0;
    *(uint32_t *)(result + 0x8) = 0;
    result = (uint32_t)((*(uint64_t *)(arg1 + 0x2F8)) - (*(uint32_t *)(arg1 + 0x1D8)));
    Arg3 = (*(uint64_t *)(arg1 + 0x2F8)) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((result) - ((uint32_t)(Arg3)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x10))) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))));
    result = (uint32_t)((result) + (Arg2));
    *(uint32_t *)(arg1 + 0x300) = (uint32_t)(result);
loc_004BC1C2:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_004BC1CC:
    goto loc_004BC1C2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1C8` | `32` | `R` |
| `Arg1` | `+ 0x1D0` | `32` | `R` |
| `Arg1` | `+ 0x1D8` | `32` | `R` |
| `Arg1` | `+ 0x2F8` | `64` | `R` |
| `Arg1` | `+ 0x2F8` | `64` | `W` |
| `Arg1` | `+ 0x300` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BC160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BC160[BB_004BC160]
  bb_004BC184[BB_004BC184]
  bb_004BC1C2[BB_004BC1C2]
  bb_004BC1CB[BB_004BC1CB]
  bb_004BC1CC[BB_004BC1CC]
  bb_004BC160 -->|branch| bb_004BC1CC
  bb_004BC160 -->|fallthrough| bb_004BC184
  bb_004BC184 -->|flow| bb_004BC1C2
  bb_004BC1CB -->|flow| bb_004BC1CC
  bb_004BC1CC -->|branch| bb_004BC1C2
```
