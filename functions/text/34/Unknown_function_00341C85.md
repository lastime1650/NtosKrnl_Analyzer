# sub_00341C85

- RVA: `0x00341C85`–`0x00341CD4` (길이 `79` bytes)
- VA: `0x0000000140341C85`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077700`
- 디코드: `26`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00341C9A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00341CBE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00341CC7` → [ExpFastResourceLegacyIsAcquiredShared](../65/ExpFastResourceLegacyIsAcquiredShared_function_00658C84.md) (function, `0x00658C84`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00341C85  33 FF                           xor edi, edi
00341C87  45 33 C9                        xor r9d, r9d
00341C8A  4C 8B C3                        mov r8, rbx
00341C8D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00341C92  B9 C6 01 00 00                  mov ecx, 0x1c6
00341C97  8D 57 0F                        lea edx, [rdi + 0xf]
00341C9A  E8 C1 B9 1B 00                  call 0x1404fd660
00341C9F  CC                              int3
00341CA0  44 0F 20 C0                     mov rax, cr8
00341CA4  3C 02                           cmp al, 2
00341CA6  76 1C                           jbe 0x140341cc4
00341CA8  33 FF                           xor edi, edi
00341CAA  44 0F B6 C0                     movzx r8d, al
00341CAE  33 D2                           xor edx, edx
00341CB0  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00341CB5  B9 C6 01 00 00                  mov ecx, 0x1c6
00341CBA  44 8D 4F 02                     lea r9d, [rdi + 2]
00341CBE  E8 9D B9 1B 00                  call 0x1404fd660
00341CC3  CC                              int3
00341CC4  48 8B CB                        mov rcx, rbx
00341CC7  E8 B8 6F 31 00                  call 0x140658c84
00341CCC  48 83 C4 58                     add rsp, 0x58
00341CD0  5F                              pop rdi
00341CD1  5B                              pop rbx
00341CD2  C3                              ret
00341CD3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00341C85(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rdi = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, v_rdi + 15, v_rbx, a4);
    result = v_cr8;
    if (((unsigned __int8)(v_cr8)) >= = 2) {
        v_rdi = 0;
        a3 = (unsigned __int8)(v_cr8);
        a2 = 0;
        v_stack_p20 = 0;
        a1 = 454;
        a4 = v_rdi + 2;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ExpFastResourceLegacyIsAcquiredShared(v_rbx, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00341C85(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rdi = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, local_rdi + 15, local_rbx, Arg4);
    result = v_cr8;
    if (((uint8_t)(v_cr8)) >= = 2) {
        local_rdi = 0;
        Arg3 = (uint8_t)(v_cr8);
        Arg2 = 0;
        v_stack_p20 = 0;
        Arg1 = 454;
        Arg4 = local_rdi + 2;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExpFastResourceLegacyIsAcquiredShared(local_rbx, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00341C85&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00341C85[BB_00341C85]
  bb_00341CA8[BB_00341CA8]
  bb_00341CC4[BB_00341CC4]
  bb_00341CD3[BB_00341CD3]
  bb_00341C85 -->|branch| bb_00341CC4
  bb_00341C85 -->|fallthrough| bb_00341CA8
  bb_00341CA8 -->|flow| bb_00341CC4
```
