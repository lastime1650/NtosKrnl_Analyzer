# x86BiosReadCmosPort

- RVA: `0x00547D64`–`0x00547DDD` (길이 `121` bytes)
- VA: `0x0000000140547D64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `38`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00547D80` → [x86BiosReadCmosPortByte](x86BiosReadCmosPortByte_function_00547DE4.md) (function, `0x00547DE4`)
- `0x00547D94` → [x86BiosReadCmosPortByte](x86BiosReadCmosPortByte_function_00547DE4.md) (function, `0x00547DE4`)
- `0x00547DA8` → [x86BiosReadCmosPortByte](x86BiosReadCmosPortByte_function_00547DE4.md) (function, `0x00547DE4`)
- `0x00547DB6` → [x86BiosReadCmosPortByte](x86BiosReadCmosPortByte_function_00547DE4.md) (function, `0x00547DE4`)

### Direct callers
- [x86BiosReadIoSpace](../47/x86BiosReadIoSpace_function_00473850.md) at `0x004738E0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00547D64  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00547D69  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00547D6E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00547D73  57                              push rdi
00547D74  48 83 EC 20                     sub rsp, 0x20
00547D78  8B D9                           mov ebx, ecx
00547D7A  0F B7 F2                        movzx esi, dx
00547D7D  0F B7 CA                        movzx ecx, dx
00547D80  E8 5F 00 00 00                  call 0x140547de4
00547D85  0F B6 F8                        movzx edi, al
00547D88  85 DB                           test ebx, ebx
00547D8A  7E 39                           jle 0x140547dc5
00547D8C  BD 01 00 00 00                  mov ebp, 1
00547D91  8D 0C 2E                        lea ecx, [rsi + rbp]
00547D94  E8 4B 00 00 00                  call 0x140547de4
00547D99  0F B6 C0                        movzx eax, al
00547D9C  C1 E0 08                        shl eax, 8
00547D9F  0B F8                           or edi, eax
00547DA1  3B DD                           cmp ebx, ebp
00547DA3  7E 20                           jle 0x140547dc5
00547DA5  8D 4E 03                        lea ecx, [rsi + 3]
00547DA8  E8 37 00 00 00                  call 0x140547de4
00547DAD  0F B6 D8                        movzx ebx, al
00547DB0  8D 4E 02                        lea ecx, [rsi + 2]
00547DB3  C1 E3 08                        shl ebx, 8
00547DB6  E8 29 00 00 00                  call 0x140547de4
00547DBB  0F B6 C8                        movzx ecx, al
00547DBE  0B CB                           or ecx, ebx
00547DC0  C1 E1 10                        shl ecx, 0x10
00547DC3  0B F9                           or edi, ecx
00547DC5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00547DCA  8B C7                           mov eax, edi
00547DCC  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00547DD1  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00547DD6  48 83 C4 20                     add rsp, 0x20
00547DDA  5F                              pop rdi
00547DDB  C3                              ret
00547DDC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall x86BiosReadCmosPort(int a1, unsigned __int16 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = x86BiosReadCmosPortByte(a2, a2, a3, a4);
    if (condition_is_less_or_equal) goto loc_00547DC5;
    result = x86BiosReadCmosPortByte(a2 + 1 * 1, a2, a3, a4);
    result = (unsigned int)(((unsigned __int8)(result)) << (8));
    v_rdi = (unsigned int)(((unsigned __int8)(result)) | ((unsigned int)(result)));
    v_rbx = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(a1))) >= = 1) {
        a1 = a2 + 3;
        result = x86BiosReadCmosPortByte(a1, a2, a3, a4);
        v_rbx = (unsigned __int8)(result);
        a1 = a2 + 2;
        v_rbx = (unsigned int)((v_rbx) << (8));
        result = x86BiosReadCmosPortByte(a1, a2, a3, a4);
        a1 = (unsigned __int8)(result);
        a1 = (unsigned int)((a1) | ((unsigned int)(v_rbx)));
        a1 = (unsigned int)((a1) << (16));
        v_rdi = (unsigned int)((v_rdi) | (a1));
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rdi));
}
```

## 5. (Beta) C Style

```c
int64_t x86BiosReadCmosPort(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = x86BiosReadCmosPortByte(Arg2, Arg2, a3, a4);
    if (condition_is_less_or_equal) goto loc_00547DC5;
    result = x86BiosReadCmosPortByte(Arg2 + 1 * 1, Arg2, a3, a4);
    result = (uint32_t)(((uint8_t)(result)) << (8));
    local_rdi = (uint32_t)(((uint8_t)(result)) | ((uint32_t)(result)));
    local_rbx = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(Arg1))) >= = 1) {
        Arg1 = Arg2 + 3;
        result = x86BiosReadCmosPortByte(Arg1, Arg2, a3, a4);
        local_rbx = (uint8_t)(result);
        Arg1 = Arg2 + 2;
        local_rbx = (uint32_t)((local_rbx) << (8));
        result = x86BiosReadCmosPortByte(Arg1, Arg2, a3, a4);
        Arg1 = (uint8_t)(result);
        Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_rbx)));
        Arg1 = (uint32_t)((Arg1) << (16));
        local_rdi = (uint32_t)((local_rdi) | (Arg1));
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rdi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rbp*1` | `32` | `R` |
| `Arg2` | `+ 0x2` | `32` | `R` |
| `Arg2` | `+ 0x3` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00547D64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00547D64[BB_00547D64]
  bb_00547D8C[BB_00547D8C]
  bb_00547DA5[BB_00547DA5]
  bb_00547DC5[BB_00547DC5]
  bb_00547DDC[BB_00547DDC]
  bb_00547D64 -->|branch| bb_00547DC5
  bb_00547D64 -->|fallthrough| bb_00547D8C
  bb_00547D8C -->|branch| bb_00547DC5
  bb_00547D8C -->|fallthrough| bb_00547DA5
  bb_00547DA5 -->|flow| bb_00547DC5
```
