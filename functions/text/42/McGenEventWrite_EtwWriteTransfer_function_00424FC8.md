# McGenEventWrite_EtwWriteTransfer

- RVA: `0x00424FC8`–`0x00425028` (길이 `96` bytes)
- VA: `0x0000000140424FC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0478`
- 디코드: `28`개 명령, `96/96` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **65**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042500D` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [McTemplateK0zd_EtwWriteTransfer](McTemplateK0zd_EtwWriteTransfer_function_004230CC.md) at `0x0042314C`
- [McTemplateK0dz_EtwWriteTransfer](McTemplateK0dz_EtwWriteTransfer_function_0042316C.md) at `0x004231F8`
- [McTemplateK0zzjzitd_EtwWriteTransfer](McTemplateK0zzjzitd_EtwWriteTransfer_function_00423218.md) at `0x00423326`
- [McTemplateK0d_EtwWriteTransfer](McTemplateK0d_EtwWriteTransfer_function_00423380.md) at `0x004233C7`
- [McTemplateK0zzjzzzdd_EtwWriteTransfer](McTemplateK0zzjzzzdd_EtwWriteTransfer_function_004233E8.md) at `0x00423552`
- [McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer](McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTrans_function_004235B8.md) at `0x00423CBE`
- [McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer](McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer_function_00423CE4.md) at `0x00424192`
- [McTemplateK0jzt_EtwWriteTransfer](McTemplateK0jzt_EtwWriteTransfer_function_00424358.md) at `0x004243DB`
- [McTemplateK0zzd_EtwWriteTransfer](McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) at `0x004244D9`
- [McTemplateK0jhzr1_EtwWriteTransfer](McTemplateK0jhzr1_EtwWriteTransfer_function_00424504.md) at `0x00424564`
- [McTemplateU0qqzr1qzr3qqxqpqqzr11q_EtwWriteTransfer](McTemplateU0qqzr1qzr3qqxqpqqzr11q_EtwWriteTransfer_function_004247D8.md) at `0x00424934`
- [McTemplateK0zq_EtwWriteTransfer](McTemplateK0zq_EtwWriteTransfer_function_00424958.md) at `0x004249D1`
- [McTemplateU0qqzr1qzr3qqqqpqqzr11_EtwWriteTransfer](McTemplateU0qqzr1qzr3qqqqpqqzr11_EtwWriteTransfer_function_00424AEC.md) at `0x00424C2F`
- [McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer](McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer_function_00424C50.md) at `0x00424F34`
- [McTemplateK0pqzzzzzzz_EtwWriteTransfer](../4B/McTemplateK0pqzzzzzzz_EtwWriteTransfer_function_004BEFF4.md) at `0x004BF1EA`
- [McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer](../4C/McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer_function_004CEF9C.md) at `0x004CF305`
- [McTemplateK0p_EtwWriteTransfer](../4D/McTemplateK0p_EtwWriteTransfer_function_004D2F24.md) at `0x004D2F68`
- [McTemplateK0z_EtwWriteTransfer](../4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) at `0x004DEFD6`
- [McTemplateK0xxxxxxxxxxxxxxxxxxq_EtwWriteTransfer](../4F/McTemplateK0xxxxxxxxxxxxxxxxxxq_EtwWriteTransfer_function_004F7528.md) at `0x004F76E6`
- [McTemplateK0j_EtwWriteTransfer](../57/McTemplateK0j_EtwWriteTransfer_function_0057B2AC.md) at `0x0057B2E4`
- [McTemplateK0jjq_EtwWriteTransfer](../58/McTemplateK0jjq_EtwWriteTransfer_function_00582D3C.md) at `0x00582DA0`
- [McTemplateK0jjtq_EtwWriteTransfer](../58/McTemplateK0jjtq_EtwWriteTransfer_function_00582DC4.md) at `0x00582E32`
- [McTemplateK0xxq_EtwWriteTransfer](../58/McTemplateK0xxq_EtwWriteTransfer_function_00582E54.md) at `0x00582EBB`
- [McTemplateK0xxxqq_EtwWriteTransfer](../58/McTemplateK0xxxqq_EtwWriteTransfer_function_00582EDC.md) at `0x00582F5B`
- [McTemplateK0jq_EtwWriteTransfer](../58/McTemplateK0jq_EtwWriteTransfer_function_00583238.md) at `0x00583289`
- [McTemplateK0xxxqqqq_EtwWriteTransfer](../58/McTemplateK0xxxqqqq_EtwWriteTransfer_function_005832A8.md) at `0x00583349`
- [McTemplateK0_EtwWriteTransfer](../59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) at `0x00596B4A`
- [McTemplateK0q_EtwWriteTransfer](../59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) at `0x00596BA8`
- [McTemplateK0jhzr1d_EtwWriteTransfer](../59/McTemplateK0jhzr1d_EtwWriteTransfer_function_00597748.md) at `0x005977C1`
- [McTemplateK0hzr0_EtwWriteTransfer](../59/McTemplateK0hzr0_EtwWriteTransfer_function_00598024.md) at `0x0059808B`
- [McTemplateK0hzr0hzr2_EtwWriteTransfer](../59/McTemplateK0hzr0hzr2_EtwWriteTransfer_function_005980AC.md) at `0x0059812E`
- [McTemplateK0dzd_EtwWriteTransfer](../5A/McTemplateK0dzd_EtwWriteTransfer_function_005A4538.md) at `0x005A45CC`
- [McTemplateK0qhzr1jxjhzr6_EtwWriteTransfer](../5A/McTemplateK0qhzr1jxjhzr6_EtwWriteTransfer_function_005A58C0.md) at `0x005A5989`
- [McTemplateK0hzr0qqhzr4_EtwWriteTransfer](../5A/McTemplateK0hzr0qqhzr4_EtwWriteTransfer_function_005A5C08.md) at `0x005A5CB5`
- [McTemplateK0izzx_EtwWriteTransfer](../5A/McTemplateK0izzx_EtwWriteTransfer_function_005A6134.md) at `0x005A620C`
- [McTemplateK0izzxqjddjz_EtwWriteTransfer](../5A/McTemplateK0izzxqjddjz_EtwWriteTransfer_function_005A6238.md) at `0x005A639A`
- [McTemplateK0zqdi_EtwWriteTransfer](../5A/McTemplateK0zqdi_EtwWriteTransfer_function_005A6944.md) at `0x005A69EB`
- [McTemplateK0pzz_EtwWriteTransfer](../5A/McTemplateK0pzz_EtwWriteTransfer_function_005A6BF8.md) at `0x005A6CBA`
- [McTemplateK0qhzr1z_EtwWriteTransfer](../5A/McTemplateK0qhzr1z_EtwWriteTransfer_function_005A6CDC.md) at `0x005A6D8F`
- [McTemplateK0zzzzz_EtwWriteTransfer](../5A/McTemplateK0zzzzz_EtwWriteTransfer_function_005A6DB0.md) at `0x005A6EF9`
- [McTemplateK0pzzqdqd_EtwWriteTransfer](../5A/McTemplateK0pzzqdqd_EtwWriteTransfer_function_005A6FD8.md) at `0x005A70DC`
- [McTemplateK0jqzjzx_EtwWriteTransfer](../5A/McTemplateK0jqzjzx_EtwWriteTransfer_function_005A7270.md) at `0x005A735F`
- [McTemplateK0qqzqqjqzjztd_EtwWriteTransfer](../5A/McTemplateK0qqzqqjqzjztd_EtwWriteTransfer_function_005A7388.md) at `0x005A751A`
- [McTemplateK0qqzqqjqzjztx_EtwWriteTransfer](../5A/McTemplateK0qqzqqjqzjztx_EtwWriteTransfer_function_005A7548.md) at `0x005A76DA`
- [McTemplateK0qqzqqtjqzjzttx_EtwWriteTransfer](../5A/McTemplateK0qqzqqtjqzjzttx_EtwWriteTransfer_function_005A7708.md) at `0x005A78CC`
- [McTemplateK0zjdd_EtwWriteTransfer](../5A/McTemplateK0zjdd_EtwWriteTransfer_function_005A7BDC.md) at `0x005A7C7B`
- [McTemplateK0zdq_EtwWriteTransfer](../5A/McTemplateK0zdq_EtwWriteTransfer_function_005A8288.md) at `0x005A830D`
- [McTemplateK0zjqdtd_EtwWriteTransfer](../5A/McTemplateK0zjqdtd_EtwWriteTransfer_function_005A8528.md) at `0x005A85EF`
- [McTemplateK0zqz_EtwWriteTransfer](../5A/McTemplateK0zqz_EtwWriteTransfer_function_005A8610.md) at `0x005A86DA`
- [McTemplateK0zz_EtwWriteTransfer](../5A/McTemplateK0zz_EtwWriteTransfer_function_005A9408.md) at `0x005A94B9`
- [McTemplateK0zzq_EtwWriteTransfer](../5A/McTemplateK0zzq_EtwWriteTransfer_function_005A94D8.md) at `0x005A959D`
- [McTemplateK0zzqq_EtwWriteTransfer](../5A/McTemplateK0zzqq_EtwWriteTransfer_function_005A95C0.md) at `0x005A9691`
- [McTemplateK0zzz_EtwWriteTransfer](../5A/McTemplateK0zzz_EtwWriteTransfer_function_005A96BC.md) at `0x005A97AA`
- [McTemplateK0zzzd_EtwWriteTransfer](../5A/McTemplateK0zzzd_EtwWriteTransfer_function_005A97D4.md) at `0x005A98C9`
- [McTemplateK0zzzdzzq_EtwWriteTransfer](../5A/McTemplateK0zzzdzzq_EtwWriteTransfer_function_005A98F8.md) at `0x005A9A61`
- [McTemplateK0zzzt_EtwWriteTransfer](../5A/McTemplateK0zzzt_EtwWriteTransfer_function_005A9A94.md) at `0x005A9B8A`
- [McTemplateK0zzztdd_EtwWriteTransfer](../5A/McTemplateK0zzztdd_EtwWriteTransfer_function_005A9BB4.md) at `0x005A9CCA`
- [McTemplateK0zzzzdd_EtwWriteTransfer](../5A/McTemplateK0zzzzdd_EtwWriteTransfer_function_005A9CF4.md) at `0x005A9E2D`
- [McTemplateK0zzqqzttquqqzxt_EtwWriteTransfer](../5A/McTemplateK0zzqqzttquqqzxt_EtwWriteTransfer_function_005A9F58.md) at `0x005AA132`
- [McTemplateK0zzqqzttquxt_EtwWriteTransfer](../5A/McTemplateK0zzqqzttquxt_EtwWriteTransfer_function_005AA160.md) at `0x005AA2D1`
- [McTemplateU0qqqqzr3_EtwWriteTransfer](../60/McTemplateU0qqqqzr3_EtwWriteTransfer_function_00605914.md) at `0x006059B3`
- [McTemplateU0qqzr1qzr3qqqxqpqqqzr13q_EtwWriteTransfer](../60/McTemplateU0qqzr1qzr3qqqxqpqqqzr13q_EtwWriteTransfer_function_006059D4.md) at `0x00605B65`
- [McTemplateU0qqzr1qzr3qqqxqqqpqzr13q_EtwWriteTransfer](../60/McTemplateU0qqzr1qzr3qqqxqqqpqzr13q_EtwWriteTransfer_function_00605B88.md) at `0x00605D0F`
- [McTemplateK0dszud_EtwWriteTransfer](../61/McTemplateK0dszud_EtwWriteTransfer_function_006183FC.md) at `0x006184E8`
- [McTemplateK0hzr0d_EtwWriteTransfer](../6A/McTemplateK0hzr0d_EtwWriteTransfer_function_006A8418.md) at `0x006A8487`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00424FC8  40 53                           push rbx
00424FCA  48 83 EC 40                     sub rsp, 0x40
00424FCE  4C 8B 51 08                     mov r10, qword ptr [rcx + 8]
00424FD2  41 8B D9                        mov ebx, r9d
00424FD5  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00424FDA  4D 85 D2                        test r10, r10
00424FDD  75 3A                           jne 0x140425019
00424FDF  4C 21 10                        and qword ptr [rax], r10
00424FE2  45 33 DB                        xor r11d, r11d
00424FE5  45 33 C9                        xor r9d, r9d
00424FE8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00424FED  44 89 48 08                     mov dword ptr [rax + 8], r9d
00424FF1  45 33 C9                        xor r9d, r9d
00424FF4  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00424FF8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00424FFE  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00425003  45 33 C0                        xor r8d, r8d
00425006  44 89 58 0C                     mov dword ptr [rax + 0xc], r11d
0042500A  48 8B 09                        mov rcx, qword ptr [rcx]
0042500D  E8 BE A0 E3 FF                  call 0x14025f0d0
00425012  48 83 C4 40                     add rsp, 0x40
00425016  5B                              pop rbx
00425017  C3                              ret
00425018  CC                              int3
00425019  4C 89 10                        mov qword ptr [rax], r10
0042501C  41 BB 02 00 00 00               mov r11d, 2
00425022  45 0F B7 0A                     movzx r9d, word ptr [r10]
00425026  EB C0                           jmp 0x140424fe8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McGenEventWrite_EtwWriteTransfer(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_00425019;
    v_r11 = 0;
    a4 = 0;
loc_00424FE8:
    v_stack_m10 = a5;
    *(unsigned int *)(a5 + 8) = 0;
    a4 = 0;
    v_stack_m18 = (unsigned int)((unsigned int)(a4));
    v_stack_m28 = a3;
    a3 = 0;
    *(unsigned int *)(a5 + 12) = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(a1), a2, a3, a4);
    v_rsp = (v_rsp) + (64);
    return result;
loc_00425019:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1 + 8);
    goto loc_00424FE8;
}
```

## 5. (Beta) C Style

```c
int64_t McGenEventWrite_EtwWriteTransfer(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_00425019;
    local_r11 = 0;
    Arg4 = 0;
loc_00424FE8:
    v_stack_m10 = Arg5;
    *(uint32_t *)(arg5 + 0x8) = 0;
    Arg4 = 0;
    v_stack_m18 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m28 = Arg3;
    Arg3 = 0;
    *(uint32_t *)(arg5 + 0xC) = 0;
    result = EtwWriteEx(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (64);
    return result;
loc_00425019:
    *(uint64_t *)(result) = *(uint64_t *)(arg1 + 0x8);
    goto loc_00424FE8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R/W` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x8` | `32` | `W` |
| `Arg5` | `+ 0xC` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00424FC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00424FC8[BB_00424FC8]
  bb_00424FDF[BB_00424FDF]
  bb_00424FE8[BB_00424FE8]
  bb_00425018[BB_00425018]
  bb_00425019[BB_00425019]
  bb_00424FC8 -->|branch| bb_00425019
  bb_00424FC8 -->|fallthrough| bb_00424FDF
  bb_00424FDF -->|flow| bb_00424FE8
  bb_00425018 -->|flow| bb_00425019
  bb_00425019 -->|branch| bb_00424FE8
```
