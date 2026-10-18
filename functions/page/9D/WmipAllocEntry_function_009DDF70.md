# WmipAllocEntry

- RVA: `0x009DDF70`–`0x009DDFBE` (길이 `78` bytes)
- VA: `0x00000001409DDF70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `24`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009DDF80` → [ExAllocateFromPagedLookasideList](../../text/3F/ExAllocateFromPagedLookasideList_function_003FB730.md) (function, `0x003FB730`)
- `0x009DDF96` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [WmipAddMofResource](../7B/WmipAddMofResource_function_007B4188.md) at `0x007B41D0`
- [WmipUpdateAddGuid](../7B/WmipUpdateAddGuid_function_007B46C0.md) at `0x007B46EC`
- [WmipUpdateModifyGuid](../7B/WmipUpdateModifyGuid_function_007B4798.md) at `0x007B4819`
- [WmipAllocGuidEntry](WmipAllocGuidEntry_function_009DD93C.md) at `0x009DD977`
- [WmipAddDataSource](WmipAddDataSource_function_009DDC30.md) at `0x009DDCB3`
- [WmipAddDataSource](WmipAddDataSource_function_009DDC30.md) at `0x009DDE2C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009DDF80` → [ExAllocateFromPagedLookasideList](../../text/3F/ExAllocateFromPagedLookasideList_function_003FB730.md) (`PAGE` → `.text`)
  - `0x009DDF96` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009DDF70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009DDF75  57                              push rdi
009DDF76  48 83 EC 20                     sub rsp, 0x20
009DDF7A  48 8B F9                        mov rdi, rcx
009DDF7D  48 8B 09                        mov rcx, qword ptr [rcx]
009DDF80  E8 AB D7 A1 FF                  call 0x1403fb730
009DDF85  48 8B D8                        mov rbx, rax
009DDF88  48 85 C0                        test rax, rax
009DDF8B  74 22                           je 0x1409ddfaf
009DDF8D  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
009DDF91  33 D2                           xor edx, edx
009DDF93  48 8B C8                        mov rcx, rax
009DDF96  E8 A5 8C CE FF                  call 0x1406c6c40
009DDF9B  48 C7 43 18 01 00 00 00         mov qword ptr [rbx + 0x18], 1
009DDFA3  8B 57 18                        mov edx, dword ptr [rdi + 0x18]
009DDFA6  89 53 10                        mov dword ptr [rbx + 0x10], edx
009DDFA9  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
009DDFAC  89 4B 20                        mov dword ptr [rbx + 0x20], ecx
009DDFAF  48 8B C3                        mov rax, rbx
009DDFB2  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009DDFB7  48 83 C4 20                     add rsp, 0x20
009DDFBB  5F                              pop rdi
009DDFBC  C3                              ret
009DDFBD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipAllocEntry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAllocateFromPagedLookasideList(*(unsigned __int64 *)(a1), a2, a3, a4);
    if (result != 0) {
        a3 = *(unsigned int *)(a1 + 8);
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, a4);
        *(unsigned __int64 *)(result + 24) = 1;
        a2 = *(unsigned int *)(a1 + 24);
        *(unsigned int *)(result + 16) = a2;
        a1 = *(unsigned int *)(a1 + 28);
        *(unsigned int *)(result + 32) = (unsigned int)(a1);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WmipAllocEntry(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAllocateFromPagedLookasideList(*(uint64_t *)(arg1), Arg2, a3, a4);
    if (result != 0) {
        a3 = *(uint32_t *)(arg1 + 0x8);
        Arg2 = 0;
        Arg1 = result;
        result = memset(Arg1, Arg2, a3, a4);
        *(uint64_t *)(result + 0x18) = 1;
        Arg2 = *(uint32_t *)(arg1 + 0x18);
        *(uint32_t *)(result + 0x10) = Arg2;
        Arg1 = *(uint32_t *)(arg1 + 0x1C);
        *(uint32_t *)(result + 0x20) = (uint32_t)(Arg1);
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
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DDF70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009DDF70[BB_009DDF70]
  bb_009DDF8D[BB_009DDF8D]
  bb_009DDFAF[BB_009DDFAF]
  bb_009DDFBD[BB_009DDFBD]
  bb_009DDF70 -->|branch| bb_009DDFAF
  bb_009DDF70 -->|fallthrough| bb_009DDF8D
  bb_009DDF8D -->|flow| bb_009DDFAF
```
