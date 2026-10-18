# XmIretOp

- RVA: `0x00577B90`–`0x00577BEB` (길이 `91` bytes)
- VA: `0x0000000140577B90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `27`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00577BAB` → [XmPopStack](../47/XmPopStack_function_00472588.md) (function, `0x00472588`)
- `0x00577BB6` → [XmPopStack](../47/XmPopStack_function_00472588.md) (function, `0x00472588`)
- `0x00577BC2` → [XmPopStack](../47/XmPopStack_function_00472588.md) (function, `0x00472588`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00577BDA` → RVA `0x00E11814` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00577B90  40 53                           push rbx
00577B92  48 83 EC 20                     sub rsp, 0x20
00577B96  8A 81 8A 00 00 00               mov al, byte ptr [rcx + 0x8a]
00577B9C  48 8B D9                        mov rbx, rcx
00577B9F  F6 D8                           neg al
00577BA1  1B D2                           sbb edx, edx
00577BA3  83 E2 02                        and edx, 2
00577BA6  FF C2                           inc edx
00577BA8  89 51 78                        mov dword ptr [rcx + 0x78], edx
00577BAB  E8 D8 A9 EF FF                  call 0x140472588
00577BB0  48 8B CB                        mov rcx, rbx
00577BB3  89 43 14                        mov dword ptr [rbx + 0x14], eax
00577BB6  E8 CD A9 EF FF                  call 0x140472588
00577BBB  48 8B CB                        mov rcx, rbx
00577BBE  66 89 43 3A                     mov word ptr [rbx + 0x3a], ax
00577BC2  E8 C1 A9 EF FF                  call 0x140472588
00577BC7  89 43 10                        mov dword ptr [rbx + 0x10], eax
00577BCA  B8 FF FF 00 00                  mov eax, 0xffff
00577BCF  39 43 14                        cmp dword ptr [rbx + 0x14], eax
00577BD2  75 10                           jne 0x140577be4
00577BD4  66 39 43 3A                     cmp word ptr [rbx + 0x3a], ax
00577BD8  75 0A                           jne 0x140577be4
00577BDA  C7 05 30 9C 89 00 01 00 00 00   mov dword ptr [rip + 0x899c30], 1
00577BE4  48 83 C4 20                     add rsp, 0x20
00577BE8  5B                              pop rbx
00577BE9  C3                              ret
00577BEA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmIretOp(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 138)));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) + 1);
    *(unsigned int *)(a1 + 120) = a2;
    result = XmPopStack(a1, a2, a3, a4);
    *(unsigned int *)(a1 + 20) = (unsigned int)(result);
    result = XmPopStack(a1, a2, a3, a4);
    *(unsigned __int16 *)(a1 + 58) = (unsigned __int16)(result);
    result = XmPopStack(a1, a2, a3, a4);
    *(unsigned int *)(a1 + 16) = (unsigned int)(result);
    if ((*(unsigned int *)(a1 + 20)) != ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_00577BE4;
    if ((*(unsigned __int16 *)(a1 + 58)) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        *(unsigned int *)(v_rip + 9018416) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xFFFFULL);
}
```

## 5. (Beta) C Style

```c
int64_t XmIretOp(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x8A)));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint32_t *)(arg1 + 0x78) = Arg2;
    result = XmPopStack(Arg1, Arg2, a3, a4);
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)(result);
    result = XmPopStack(Arg1, Arg2, a3, a4);
    *(uint16_t *)(arg1 + 0x3A) = (uint16_t)(result);
    result = XmPopStack(Arg1, Arg2, a3, a4);
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
    if ((*(uint32_t *)(arg1 + 0x14)) != ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_00577BE4;
    if ((*(uint16_t *)(arg1 + 0x3A)) == ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        *(uint32_t *)(v_rip + 0x899C30) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xFFFFULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x3A` | `16` | `R` |
| `Arg1` | `+ 0x3A` | `16` | `W` |
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg1` | `+ 0x8A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00577B90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00577B90[BB_00577B90]
  bb_00577BD4[BB_00577BD4]
  bb_00577BDA[BB_00577BDA]
  bb_00577BE4[BB_00577BE4]
  bb_00577BEA[BB_00577BEA]
  bb_00577B90 -->|branch| bb_00577BE4
  bb_00577B90 -->|fallthrough| bb_00577BD4
  bb_00577BD4 -->|branch| bb_00577BE4
  bb_00577BD4 -->|fallthrough| bb_00577BDA
  bb_00577BDA -->|flow| bb_00577BE4
```
