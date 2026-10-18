# VfZwDeviceIoControlFile_Entry

- RVA: `0x00BA43F0`–`0x00BA444D` (길이 `93` bytes)
- VA: `0x0000000140BA43F0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `27`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA43F9` → [ViZwShouldCheck](ViZwShouldCheck_function_00BA4DB4.md) (function, `0x00BA4DB4`)
- `0x00BA4409` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA4415` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA4421` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA442D` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA4439` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA4441` → [ViZwCheckApcRequirement](ViZwCheckApcRequirement_function_00BA4C18.md) (function, `0x00BA4C18`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA43F0  40 53                           push rbx
00BA43F2  48 83 EC 20                     sub rsp, 0x20
00BA43F6  48 8B D9                        mov rbx, rcx
00BA43F9  E8 B6 09 00 00                  call 0x140ba4db4
00BA43FE  85 C0                           test eax, eax
00BA4400  74 44                           je 0x140ba4446
00BA4402  48 8B 13                        mov rdx, qword ptr [rbx]
00BA4405  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
00BA4409  E8 5A 09 00 00                  call 0x140ba4d68
00BA440E  48 8B 13                        mov rdx, qword ptr [rbx]
00BA4411  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00BA4415  E8 4E 09 00 00                  call 0x140ba4d68
00BA441A  48 8B 13                        mov rdx, qword ptr [rbx]
00BA441D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00BA4421  E8 42 09 00 00                  call 0x140ba4d68
00BA4426  48 8B 13                        mov rdx, qword ptr [rbx]
00BA4429  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00BA442D  E8 36 09 00 00                  call 0x140ba4d68
00BA4432  48 8B 13                        mov rdx, qword ptr [rbx]
00BA4435  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00BA4439  E8 2A 09 00 00                  call 0x140ba4d68
00BA443E  48 8B 0B                        mov rcx, qword ptr [rbx]
00BA4441  E8 D2 07 00 00                  call 0x140ba4c18
00BA4446  48 83 C4 20                     add rsp, 0x20
00BA444A  5B                              pop rbx
00BA444B  C3                              ret
00BA444C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfZwDeviceIoControlFile_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ViZwShouldCheck(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 56);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 32);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(a1);
        result = ViZwCheckApcRequirement(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfZwDeviceIoControlFile_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ViZwShouldCheck(Arg1, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x38);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        Arg1 = *(uint64_t *)(arg1);
        result = ViZwCheckApcRequirement(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA43F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA43F0[BB_00BA43F0]
  bb_00BA4402[BB_00BA4402]
  bb_00BA4446[BB_00BA4446]
  bb_00BA444C[BB_00BA444C]
  bb_00BA43F0 -->|branch| bb_00BA4446
  bb_00BA43F0 -->|fallthrough| bb_00BA4402
  bb_00BA4402 -->|flow| bb_00BA4446
```
