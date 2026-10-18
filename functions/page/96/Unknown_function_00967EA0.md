# sub_00967EA0

- RVA: `0x00967EA0`–`0x00967F06` (길이 `102` bytes)
- VA: `0x0000000140967EA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095158`
- 디코드: `28`개 명령, `102/102` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00967EB4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00967ECA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00967EDE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00967EEC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00967EB4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00967ECA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00967EDE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00967EEC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00967EAC` → [sub_00968AEF](Unknown_function_00968AEF.md) (`tail-transfer`)
  - `0x00967F04` → [sub_00967F06 + 0xA](Unknown_function_00967F06.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00967EA0  4D 85 ED                        test r13, r13
00967EA3  74 4C                           je 0x140967ef1
00967EA5  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00967EA9  48 85 C9                        test rcx, rcx
00967EAC  0F 84 3D 0C 00 00               je 0x140968aef
00967EB2  33 D2                           xor edx, edx
00967EB4  E8 B7 A9 21 00                  call 0x140b82870
00967EB9  33 F6                           xor esi, esi
00967EBB  49 89 75 08                     mov qword ptr [r13 + 8], rsi
00967EBF  49 8B 4D 18                     mov rcx, qword ptr [r13 + 0x18]
00967EC3  48 85 C9                        test rcx, rcx
00967EC6  74 0B                           je 0x140967ed3
00967EC8  33 D2                           xor edx, edx
00967ECA  E8 A1 A9 21 00                  call 0x140b82870
00967ECF  49 89 75 18                     mov qword ptr [r13 + 0x18], rsi
00967ED3  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
00967ED7  48 85 C9                        test rcx, rcx
00967EDA  74 0B                           je 0x140967ee7
00967EDC  33 D2                           xor edx, edx
00967EDE  E8 8D A9 21 00                  call 0x140b82870
00967EE3  49 89 75 28                     mov qword ptr [r13 + 0x28], rsi
00967EE7  33 D2                           xor edx, edx
00967EE9  49 8B CD                        mov rcx, r13
00967EEC  E8 7F A9 21 00                  call 0x140b82870
00967EF1  4C 8B AC 24 38 02 00 00         mov r13, qword ptr [rsp + 0x238]
00967EF9  48 8B B4 24 48 02 00 00         mov rsi, qword ptr [rsp + 0x248]
00967F01  4D 85 FF                        test r15, r15
00967F04  74 0A                           je 0x140967f10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00967EA0(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45, __int64 a46, __int64 a47, __int64 a48, __int64 a49, __int64 a50, __int64 a51, __int64 a52, __int64 a53, __int64 a54, __int64 a55, __int64 a56, __int64 a57, __int64 a58, __int64 a59, __int64 a60, __int64 a61, __int64 a62, __int64 a63, __int64 a64, __int64 a65, __int64 a66, __int64 a67, __int64 a68, __int64 a69, __int64 a70, __int64 a71, __int64 a72, __int64 a73)
{
    __int64 result;
    __int64 v_rsi;

    if (v_r13 == 0) goto loc_00967EF1;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_r13 + 8), a2, a3, a4);
    v_rsi = 0;
    *(unsigned __int64 *)(v_r13 + 8) = 0;
    if (*(unsigned __int64 *)(v_r13 + 24) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_r13 + 24), a2, a3, a4);
        *(unsigned __int64 *)(v_r13 + 24) = 0;
    }
    if (*(unsigned __int64 *)(v_r13 + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_r13 + 40), a2, a3, a4);
        *(unsigned __int64 *)(v_r13 + 40) = 0;
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_r13, a2, a3, a4);
loc_00967EF1:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00967EA0(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, uint64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, uint64_t Arg41, uint64_t Arg42, uint64_t Arg43, uint64_t Arg44, uint64_t Arg45, uint64_t Arg46, uint64_t Arg47, uint64_t Arg48, uint64_t Arg49, uint64_t Arg50, uint64_t Arg51, uint64_t Arg52, uint64_t Arg53, uint64_t Arg54, uint64_t Arg55, uint64_t Arg56, uint64_t Arg57, uint64_t Arg58, uint64_t Arg59, uint64_t Arg60, uint64_t Arg61, uint64_t Arg62, uint64_t Arg63, uint64_t Arg64, uint64_t Arg65, uint64_t Arg66, uint64_t Arg67, uint64_t Arg68, uint64_t Arg69, uint64_t Arg70, int64_t Arg71, uint64_t Arg72, int64_t Arg73)
{
    int64_t result;
    int64_t local_rsi;

    if (local_r13 == 0) goto loc_00967EF1;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_r13 + 0x8), Arg2, Arg3, Arg4);
    local_rsi = 0;
    *(uint64_t *)(local_r13 + 0x8) = 0;
    if (*(uint64_t *)(local_r13 + 0x18) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_r13 + 0x18), Arg2, Arg3, Arg4);
        *(uint64_t *)(local_r13 + 0x18) = 0;
    }
    if (*(uint64_t *)(local_r13 + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_r13 + 0x28), Arg2, Arg3, Arg4);
        *(uint64_t *)(local_r13 + 0x28) = 0;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r13, Arg2, Arg3, Arg4);
loc_00967EF1:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00967EA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00967EA0[BB_00967EA0]
  bb_00967EA5[BB_00967EA5]
  bb_00967EB2[BB_00967EB2]
  bb_00967EC8[BB_00967EC8]
  bb_00967ED3[BB_00967ED3]
  bb_00967EDC[BB_00967EDC]
  bb_00967EE7[BB_00967EE7]
  bb_00967EF1[BB_00967EF1]
  bb_00967EA0 -->|branch| bb_00967EF1
  bb_00967EA0 -->|fallthrough| bb_00967EA5
  bb_00967EA5 -->|fallthrough| bb_00967EB2
  bb_00967EB2 -->|branch| bb_00967ED3
  bb_00967EB2 -->|fallthrough| bb_00967EC8
  bb_00967EC8 -->|flow| bb_00967ED3
  bb_00967ED3 -->|branch| bb_00967EE7
  bb_00967ED3 -->|fallthrough| bb_00967EDC
  bb_00967EDC -->|flow| bb_00967EE7
  bb_00967EE7 -->|flow| bb_00967EF1
```
