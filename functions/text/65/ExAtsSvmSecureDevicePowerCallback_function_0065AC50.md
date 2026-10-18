# ExAtsSvmSecureDevicePowerCallback

- RVA: `0x0065AC50`–`0x0065ACAF` (길이 `95` bytes)
- VA: `0x000000014065AC50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `29`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0065AC71` → [ExpAtsConfigureSecureDevice](ExpAtsConfigureSecureDevice_function_00659E3C.md) (function, `0x00659E3C`)
- `0x0065AC98` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065AC50  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0065AC55  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0065AC5A  57                              push rdi
0065AC5B  48 83 EC 30                     sub rsp, 0x30
0065AC5F  83 FA 01                        cmp edx, 1
0065AC62  8B DA                           mov ebx, edx
0065AC64  49 8B C8                        mov rcx, r8
0065AC67  49 8B F8                        mov rdi, r8
0065AC6A  40 0F 94 C6                     sete sil
0065AC6E  40 8A D6                        mov dl, sil
0065AC71  E8 C6 F1 FF FF                  call 0x140659e3c
0065AC76  83 FB 01                        cmp ebx, 1
0065AC79  74 23                           je 0x14065ac9e
0065AC7B  85 C0                           test eax, eax
0065AC7D  79 1F                           jns 0x14065ac9e
0065AC7F  40 0F B6 CE                     movzx ecx, sil
0065AC83  4C 8B CF                        mov r9, rdi
0065AC86  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0065AC8B  BA 02 32 00 00                  mov edx, 0x3202
0065AC90  B9 59 01 00 00                  mov ecx, 0x159
0065AC95  4C 63 C0                        movsxd r8, eax
0065AC98  E8 C3 29 EA FF                  call 0x1404fd660
0065AC9D  CC                              int3
0065AC9E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0065ACA3  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0065ACA8  48 83 C4 30                     add rsp, 0x30
0065ACAC  5F                              pop rdi
0065ACAD  C3                              ret
0065ACAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExAtsSvmSecureDevicePowerCallback(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rsi = (a2 == 1) ? 1 : 0;
    result = ExpAtsConfigureSecureDevice(a3, (unsigned __int8)(v_rsi), a3, a4);
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_0065AC9E;
    if (sign_flag) {
        a1 = (unsigned __int8)(v_rsi);
        a4 = a3;
        v_stack_m18 = a1;
        a2 = 0x3202ULL;
        a1 = 345;
        a3 = (int)((unsigned int)(result));
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExAtsSvmSecureDevicePowerCallback(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rsi = (Arg2 == 1) ? 1 : 0;
    result = ExpAtsConfigureSecureDevice(Arg3, (uint8_t)(local_rsi), Arg3, a4);
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_0065AC9E;
    if (sign_flag) {
        Arg1 = (uint8_t)(local_rsi);
        a4 = Arg3;
        v_stack_m18 = Arg1;
        Arg2 = 0x3202ULL;
        Arg1 = 345;
        Arg3 = (int32_t)((uint32_t)(result));
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065AC50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065AC50[BB_0065AC50]
  bb_0065AC7B[BB_0065AC7B]
  bb_0065AC7F[BB_0065AC7F]
  bb_0065AC9E[BB_0065AC9E]
  bb_0065ACAE[BB_0065ACAE]
  bb_0065AC50 -->|branch| bb_0065AC9E
  bb_0065AC50 -->|fallthrough| bb_0065AC7B
  bb_0065AC7B -->|branch| bb_0065AC9E
  bb_0065AC7B -->|fallthrough| bb_0065AC7F
  bb_0065AC7F -->|flow| bb_0065AC9E
```
